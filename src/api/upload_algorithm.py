from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import blobstore

from src.model import File


class UploadAlgorithmHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        user_id = self.request.get('user_id')
        # author_id = self.request.get('author_id')

        # mapper implementation
        mapper = self.get_uploads(field_name='mapper')[0]
        mapper_data = File(
            type="mapper",
            user_id=user_id,
            blob_key=mapper.key())
        mapper_data.put()

        # reducer implementation
        reducer = self.get_uploads('reducer')[0]
        reducer_data = File(
            type="reducer",
            user_id=user_id,
            blob_key=reducer.key())
        reducer_data.put()

        # what to do after files uploaded ? start data processing probably
        # self.redirect('/view_file/{0}/{1}'.format(mapper.key(), reducer.key()))
        # self.redirect("/view_file/" + str(mapper.key()) + "/" + str(reducer.key()))
        self.redirect('/')
