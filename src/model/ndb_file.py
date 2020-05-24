# we use this class for uploading mapper and reducer implementation files
# type - can be either mapper or reducer
# user_id - user that commissioned the data processing over this implementation
# author_id - author of this implementation
# blob_key - key for the uploaded file

from google.appengine.ext import ndb


# define model
class File(ndb.Model):
    type = ndb.StringProperty(default="mapper")
    user_id = ndb.StringProperty()
    author_id = ndb.StringProperty(default="")
    blob_key = ndb.BlobKeyProperty()
