import base64
import collections
import md5
import uuid
from unittest import TestCase
import webapp2
import webtest
from google.appengine.api import memcache, datastore
from google.appengine.ext import testbed

from mapreduce.main import create_handlers_map

from src.api import DeleteDataHandler, UploadAlgorithmHandler, UploadDataHandler, ProcessDataHandler


def create_app_test_handlers():
    map_reduce_handlers = create_handlers_map()
    app_handlers = [
        ('/delete_data', DeleteDataHandler),
        ('/upload_algorithms', UploadAlgorithmHandler),
        ('/upload_data', UploadDataHandler),
        ('/run_pipeline', ProcessDataHandler),
    ]
    return app_handlers + map_reduce_handlers


class TestMainView(TestCase):
    def setUp(self):
        # Create a WSGI application.
        app = webapp2.WSGIApplication(create_app_test_handlers())

        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate(True)
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_blobstore_stub()
        self.testbed.init_files_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def upload_blobstore_file(self, upload_url, field, filename, contents, type="application/octet-stream"):
        session = datastore.Get(upload_url.split('/')[-1])
        new_object = "/" + session["gs_bucket_name"] + "/" + str(uuid.uuid4())
        self.testbed._get_blob_storage().store(new_object, type, contents)

        message = "Content-Type: application/octet-stream\r\nContent-Length: " + str(
            len(contents)) + "\r\nContent-MD5: " + base64.b64encode(
            md5.new(contents).hexdigest()) + "\r\nX-AppEngine-Cloud-Storage-Object: /gs" + new_object.encode(
            "ascii") + "\r\ncontent-disposition: form-data; name=\"" + field + "\"; filename=\"" + filename\
                  + "\"\r\nX-AppEngine-Upload-Creation: 2015-07-17 16:19:55.531719\r\n\r\n"
        return self.testapp.post('/upload_data', upload_files=[
            (field, filename, message,
             "message/external-body; blob-key=\"encoded_gs_file:blablabla\"; access-type=\"X-AppEngine-BlobKey\"")
        ])

    def test_upload_data(self):
        file = testbed.
        upload_url = self.testapp.post('/upload_data').body
        response = self.upload_blobstore_file('/upload_data', "data_file", "data.json").json
        # response = self.testapp.post('/upload_data',
        #                              upload_files=[('data_file', 'data.json')])
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.content_type, 'text/plain')

    def test_run_pipeline(self):
        # First define a key and value to be cached.
        mapper = '1-rPvuKvszhBU5BcW5AqkQ=='
        reducer = '7Gcucx71YFUzPcf7gvcUxw=='
        language = 'r'
        # self.testbed.init_memcache_stub()
        params = {'mapper': mapper, 'reducer': reducer, 'language': language}
        # Then pass those values to the handler.
        response = self.testapp.post('/run_pipeline', params)
        # Finally verify that the passed-in values are actually stored in Memcache.
        self.assertEqual(response.status_int, 200)
        self.fail()
