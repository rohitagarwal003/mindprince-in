#!/usr/bin/env python

import os

import webapp2

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.redirect("/")

app = webapp2.WSGIApplication([
    ('/.*', MainHandler),
], debug=False)
