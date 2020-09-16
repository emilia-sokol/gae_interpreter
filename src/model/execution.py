from google.appengine.ext import ndb


# define execution model
class Execution(ndb.Expando):
    # we store all information about gae resources used during data processing

    type = ndb.StringProperty(default="cpu")

    # we do most data processing on values, cannot be null
    value = ndb.FloatProperty(default=0)

    # time when data was added to the system
    time = ndb.DateTimeProperty(auto_now_add=True)
