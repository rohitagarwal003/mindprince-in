#!/usr/bin/env python

import webapp2

class Redirect(webapp2.RequestHandler):
	def get(self, subdomain, path=""):
		self.redirect("http://" + subdomain + ".mindprince.in/" + path)

app = webapp2.WSGIApplication([
    ('/(blog)/(.*)', Redirect),
    ('/(notes)/(.*)', Redirect),
    ('/(.*)', Redirect),
], debug=False)

# Notes on routing
# /blog matches the third rule.
# /blog/ matches the first rule.
# /blog/anything matches the first rule.
