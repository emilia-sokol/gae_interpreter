import webapp2
import os
import datetime

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import template

# data model for interpreter module
from src.model import DisplayFile, Data, File


class MainView(webapp2.RequestHandler):
    def get(self):
        upload_mapper = blobstore.create_upload_url('/upload_file/mapper')
        upload_reducer = blobstore.create_upload_url('/upload_file/reducer')

        files = []

        for num, data in enumerate(File.query().fetch(), start=1):
            files.insert(num, DisplayFile(blobstore.BlobInfo.get(data.blob_key).filename, data.type, data.blob_key))

        template_values = {
            'data': Data.query().fetch(),
            'files': files,
        }

        template_path = os.path.join(os.path.dirname(__file__), '../static/html/main.html')

        self.response.out.write(
            # render test ui with data and uploaded files
            template.render(template_path, template_values).format(upload_mapper, upload_reducer)
        )

    def post(self):
        key = self.request.get('key')
        data_type = self.request.get('type')
        value = self.request.get('value')
        ts = datetime.datetime.utcnow()

        # save data to google storage
        Data(key=key, type=data_type, value=value, time=ts).put()

        # stay on main page
        self.redirect('/')
