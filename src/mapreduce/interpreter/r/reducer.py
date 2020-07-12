import json

from mapreduce import context
from google.appengine.ext import blobstore
import requests


def r_reducer_interpreter(key, values):
    # @TODO implementation
    # @TODO add conditional imports based on mapper requirements

    ctx = context.get()
    file_blob_key = ctx.mapreduce_spec.mapper.params['output_writer']['reducer']
    reader = blobstore.BlobReader(file_blob_key)

    reducer = reader.read()

    print("r_reducer_interpreter")
    print(key)
    print(values)

    url = 'http://127.0.0.1:9090/upload_reducer'
    data = {
        "reducer": reducer,
        "values": values
    }
    # how to send an array of strings through rest api ??
    # I'm sending an array but I get a first element on the other side :P
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    yield "%s: %s\n" % (key, str(response.text))
