import webapp2
import os
import datetime

from google.appengine.ext import blobstore
from google.appengine.ext.webapp import template

# data model for interpreter module
from src.model import DisplayFile, Data, File


class MainView(webapp2.RequestHandler):
    def get(self):
        upload_algorithms = blobstore.create_upload_url('/upload_algorithms')
        upload_data = blobstore.create_upload_url('/upload_data')

        files = []
        posts = []

        for num, data in enumerate(File.query().fetch(), start=1):
            if blobstore.BlobInfo.get(data.blob_key) is not None:
                files.insert(num, DisplayFile(
                    blobstore.BlobInfo.get(data.blob_key).filename,
                    data.type,
                    data.blob_key,
                    data.user_id,
                ))

        for num, data in enumerate(Data.query().fetch(), start=1):
            post = data

            # enhance post object with url_safe string, useful when deleting posts
            post.url_safe = data.key.urlsafe()
            posts.insert(num, post)

        template_values = {
            'data': posts,
            'files': files,
        }

        template_path = os.path.join(os.path.dirname(__file__), '../static/html/main.html')

        self.response.out.write(
            # render test ui with data and uploaded files
            template.render(template_path, template_values).format(upload_algorithms, upload_data)
        )

    def post(self):
        data_id = self.request.get('id')
        data_type = self.request.get('type')
        value = self.request.get('value')
        ts = datetime.datetime.utcnow()

        # save data to google storage
        Data(id=data_id, type=data_type, value=value, time=ts).put()

        # stay on main page
        self.redirect('/')
