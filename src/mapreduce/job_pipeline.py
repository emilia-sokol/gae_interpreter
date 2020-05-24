import logging

from mapreduce import base_handler
from mapreduce import mapreduce_pipeline

from google.appengine.api import app_identity


class JobPipeline(base_handler.PipelineBase):
    """
    Pipeline to process post data using mapper and reducer interpreters
    """

    def callback(self, **kwargs):
        # @TODO add implementation
        pass

    def finalized_test(self, *args, **kwargs):
        # @TODO add implementation
        pass

    def run_test(self, *args, **kwargs):
        # @TODO add implementation
        pass

    def run(self, mapper_key, reducer_key, file_name):
        """ run """
        logging.debug("filename is %s" % file_name)

        bucket_name = app_identity.get_default_gcs_bucket_name()
        mapper_params = {
            # @TODO test if Data model can be imported that way
            "entity_kind": "Data",
            "mapper": mapper_key,
            "reducer": reducer_key
        }

        output = yield mapreduce_pipeline.MapreducePipeline(
            file_name,
            mapper_spec="main.mapper_interpreter",
            reducer_spec="main.reducer_interpreter",
            input_reader_spec="mapreduce.input_readers.DatastoreInputReader",
            output_writer_spec="mapreduce.output_writers.GoogleCloudStorageOutputWriter",
            mapper_params=mapper_params,
            reducer_params={
                "output_writer": {
                    "reducer": reducer_key,
                    "bucket_name": bucket_name,
                    "content_type": "text/plain",
                }
            },
            shards=64)

        # @TODO store output
        # yield StoreOutput(output)
