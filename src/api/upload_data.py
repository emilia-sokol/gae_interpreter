from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore

import json
import datetime

from src.model import Data


class UploadDataHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        data = self.get_uploads(field_name='data_file')[0]
        reader = blobstore.BlobReader(data.key())

        # @TODO try to handle errors like wrong json syntax, could not parse
        json_data = json.load(reader)

        # save data
        # @TODO also here there should be an error handler for json with unacceptable structure
        for key in json_data.keys():
            post = json_data[key]
            ts = datetime.datetime.utcnow()

            if 'id' in post:
                Data(id=post['id'], type=post['type'], value=post['value'], time=ts).put()
            else:
                Data(type=post['type'], value=post['value'], time=ts).put()

        self.redirect('/')
