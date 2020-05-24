from google.appengine.ext import ndb


# define data model
class Data(ndb.Expando):
    # we store all data as key, type and value. key should be unique (but not necessarily, maybe key will be id of
    # user that sends data or/and id of a device that sends data). by type we distinguish what kind of data is this
    # e.g. temperature, text (this will be used possibly by mapper and reducer functions)

    id = ndb.StringProperty(default="")
    # user_id = ndb.StringProperty(default="")
    # device_id = ndb.StringProperty(default="")

    type = ndb.StringProperty(default="")

    # we do most data processing on values, cannot be null
    value = ndb.StringProperty(default="")

    # time when data was added to the system
    time = ndb.DateTimeProperty(auto_now_add=True)
