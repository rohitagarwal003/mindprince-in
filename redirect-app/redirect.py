#!/usr/bin/env python

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.redirect("https://www.rohitagarwal.org/")

app = webapp2.WSGIApplication([
    ('/.*', MainHandler),
], debug=False)
