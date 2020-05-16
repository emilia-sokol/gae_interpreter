import webapp2
import mapreduce


class MainView(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!\n')
        self.response.write(mapreduce.version)