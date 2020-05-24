import pipeline

from google.appengine.ext import blobstore

from src.model import Output


class StoreOutput(pipeline.Pipeline):
    """A pipeline to store the result of the MapReduce job in the database. """

    def run_test(self, *args, **kwargs):
        # @TODO add implementation
        pass

    def finalized_test(self, *args, **kwargs):
        # @TODO add implementation
        pass

    def callback(self, **kwargs):
        # @TODO add implementation
        pass

    def run(self, output):
        for out in output:
            blobstore_filename = "/gs" + out
            blobstore_gs_key = blobstore.create_gs_key(blobstore_filename)
            url_path = "/blobstore/" + blobstore_gs_key
            Output(text=url_path).put()