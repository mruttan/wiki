import os
import re
import random
import hashlib
import hmac
import logging
import json
from datetime import datetime, timedelta
from string import letters

import webapp2
import jinja2

from google.appengine.api import memcache
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
		def write(self, *a, **kw):
				self.response.write(*a, **kw)

		def render_str(self, template, **params):
				t = jinja_env.get_template(template)
				return t.render(params)

		def render(self, template, **kw):
				self.write(self.render_str(template, **kw))

class MainPage(Handler):
		def get(self):
				self.write("Hello World")
				self.render('base.html')
				

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)