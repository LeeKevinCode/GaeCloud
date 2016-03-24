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

html = """
	<!doctype html>
	<html lang="en">
		<head>
			<meta charset="utf-8"/>
			<title>Template Example</title>
		</head>
		<body>
			<p>This is correct  %d </p>

			<form method = "post">
 				First name:<br>
 				<input type="text" name="firstname" value="">
 				<br>
 				Last name:<br>
 				<input type="text" name="lastname" value="">
 				<br><br>
 				<input name="save" type="submit" value="save">
 			</form>
		</body>
	</html>
"""
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	count = 100
        self.response.write(html %count)
    def post(self):
    	firstName = self.request.get("firstname")
    	lastName = self.request.get("lastname")
    	if len(firstName) < 2 or len(lastName) < 2:
    		self.redirect("/")
    	self.response.out.write(firstName +" " + lastName)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
