import webapp2
from google.appengine.ext import ndb


class DeleteDataHandler(webapp2.RequestHandler):
    def post(self):

        # delete all selected posts
        for arg in self.request.arguments():
            reconstruct_key = ndb.Key(urlsafe=arg)
            to_delete = reconstruct_key.get()

            # delete
            to_delete.key.delete()

        self.redirect('/')
