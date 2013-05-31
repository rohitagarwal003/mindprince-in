#!/usr/bin/env python

import webapp2

class Redirect(webapp2.RequestHandler):
	def get(self, subdomain):
		self.redirect("http://" + subdomain + ".mindprince.in")

app = webapp2.WSGIApplication([
    ('/(.*)', Redirect),
], debug=True)
