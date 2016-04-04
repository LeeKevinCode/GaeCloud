#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
from google.appengine.ext import db

# A Model for a User
class User(db.Model):
    account = db.StringProperty()
    password = db.StringProperty()
    name = db.StringProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        JINJA_ENVIRONMENT = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.join(
                os.path.dirname(__file__),'templates')),
            autoescape=True)
        template = JINJA_ENVIRONMENT.get_template('applyscreen.html')
        self.response.write(template.render())

    def post(self):
        rname = self.request.get('name')
        raccount = self.request.get('account')
        rpassword = self.request.get('password')
        self.user = User(account = raccount, password = rpassword, name = rname)
        self.user.put()
        self.response.write('successfully submitted')

class ShowHandler(webapp2.RequestHandler):
    def get(self):
        JINJA_ENVIRONMENT = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.join(
                os.path.dirname(__file__),'templates')),
            autoescape=True)
        template = JINJA_ENVIRONMENT.get_template('show.html')
        user = db.Query(User)
        user_dir = {'greetings': user}                
        self.response.write(template.render(user_dir))
        
app = webapp2.WSGIApplication([
    webapp2.Route(r'/', MainHandler),
    webapp2.Route(r'/show', ShowHandler)
], debug=True)
