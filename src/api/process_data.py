from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb
from google.appengine.ext import blobstore

from src.mapreduce import JobPipeline


class ProcessDataHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def post(self):
        mapper_key = self.request.get('mapper')
        reducer_key = self.request.get('reducer')
        language = self.request.get('language')

        print(mapper_key)
        print(reducer_key)
        print(language)

        # first check if we have full algorithm implementation
        if not blobstore.get(mapper_key) or not blobstore.get(reducer_key):
            self.error(404)
        else:
            mapper_name = blobstore.BlobInfo.get(mapper_key).filename

            # run data processing
            pipeline = JobPipeline(mapper_key, reducer_key, mapper_name, language)
            pipeline.start()

            # for testing purposes uncomment line below
            # print(pipeline.pipeline_id)

            # redirect to see data process preview
            self.redirect(pipeline.base_path + "/status?root=" + pipeline.pipeline_id)
