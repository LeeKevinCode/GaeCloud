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
import os
import logging
import jinja2

from google.appengine.ext import db

class Number(db.Model):
    num = db.IntegerProperty(default = 0)

class MainHandler(webapp2.RequestHandler):
    def get(self):   
        JINJA_ENVIRONMENT = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.join(
                os.path.dirname(__file__),'templates')),
            autoescape=True)
        template = JINJA_ENVIRONMENT.get_template('index.html')
        template_values = {
            'hint': 'Please make a guess'
        }
        self.response.write(template.render(template_values))

    def post(self):
        stguess = self.request.get('guess')
        try:
            guess = int(stguess)
        except:
            guess = -1
        answer = 42
        if guess == answer:
            msg = 'Congratulations'
        elif guess < 0 :
            msg = 'Please provide a number'
        elif guess < answer:
            msg = 'Your guess is too low'
        else:
            msg = 'Your guess is too high'
        JINJA_ENVIRONMENT = jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.join(
                os.path.dirname(__file__),'templates')),
            autoescape=True)
        template = JINJA_ENVIRONMENT.get_template('guess.html')
        template_values = {
            'stguess': stguess,
            'hint': msg
        }
        self.response.write(template.render(template_values))
        self.number = Number(num = int(stguess))
        self.number.put()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
	], debug=True)


