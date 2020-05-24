from mapreduce import context
from google.appengine.ext import blobstore


def reducer_interpreter(key, values):

    ctx = context.get()
    file_blob_key = ctx.mapreduce_spec.mapper.params['output_writer']['reducer']
    reader = blobstore.BlobReader(file_blob_key)

    output = []
    exec (reader.read(), {"key": key, "values": values, "output": output})

    for out in output:
        # @TODO store output somewhere and redirect to the source after
        print(out)
        yield "%s: %d\n" % (out[0], out[1])