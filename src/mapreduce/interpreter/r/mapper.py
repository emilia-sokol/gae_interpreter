from mapreduce import context
from google.appengine.ext import blobstore
import requests


def r_mapper_interpreter(entity):
    # ctx = context.get()
    # file_blob_key = "U-mTu_kekFHkTYYJ-gHcmQ=="
    # reader = blobstore.BlobReader(file_blob_key)

    ctx = context.get()
    file_blob_key = ctx.mapreduce_spec.mapper.params['mapper']
    reader = blobstore.BlobReader(file_blob_key)

    mapper = reader.read()

    url = 'http://127.0.0.1:9090/upload'
    data = {
      "mapper": mapper,
      "entity": entity
    }
    response = requests.post(url, data=data)
    print(response)

    # yield result
