from mapreduce import context
from google.appengine.ext import blobstore


def mapper_interpreter(entity):
    # check if this is working, import module - name provided by algorithm provider
    # @TODO add conditional imports based on mapper requirements
    coll = __import__("collections")

    # interpreter = InteractiveInterpreter()
    ctx = context.get()
    file_blob_key = ctx.mapreduce_spec.mapper.params['mapper']
    reader = blobstore.BlobReader(file_blob_key)

    values = []

    exec (reader.read(), {"entity": entity, "output": values, "collections": coll, "list": list, "dict": dict})

    for value in values:
        yield value
    # yield op.db.Put(entity)
