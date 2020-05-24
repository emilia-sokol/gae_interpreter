# this class is for keeping output from mapreduce job pipline func execution
# shape of this class will most likely change

from google.appengine.ext import ndb


class Output(ndb.Model):
    text = ndb.StringProperty(default="")
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
