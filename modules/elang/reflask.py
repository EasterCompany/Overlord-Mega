# -*- coding: utf-8 -*-

# STANDARD LIBRARY IMPORTS
from os import path, system, chdir, getcwd
from sys import platform, argv
from sqlite3 import connect

# THIRD-PARTY IMPORTS
from flask import Flask, render_template, redirect, request, jsonify

# INTERNAL IMPORTS
from modules.elang.basic import make_path, StringWithColour
from modules.elang.index import overlord


""" REFLASK CLASS

  Allows for creating, installing,
  building & serving flask based
  backend applications with HTML
  and/or React-JS based front ends
"""


class ReFlask:

  def __init__(self, _name_="overlord", react_enabled=False, _sub_=False):
    # PASS IF THIS IS A "SUB" APP
    if not _sub_:
      # DIRECTORY INITIALIZATION
      make_path("./public") 							# PUBLIC Information
      make_path("./templates/site") 			# HTML/CSS/JS Objects
      make_path("./templates/pages")			# HTML/CSS/JS Templates
      # REFLASK INSTANCE OBJECTS
      self.end = Flask(_name_)						# BACK-END App
      self.rwd = getcwd() 								# ROOT Working Directory
      self.nme = _name_ 									# FRONT-END App
      # CORE FUNCTIONALITY INITIALIZATION
      if "build" in argv: 								# ON-RUN Build command
        if react_enabled:
          make_path("./static/react") 		# REACT-JS Local Cache
          chdir("apps/" + _name_) 				# GO TO App Directory
          system("npm run build") 				# RUN npm build cmd
          chdir(self.rwd) 								# GO TO Root Directory

  def run(self, debug=False): 						# Serves the Back End Web App
    self.end.register_blueprint(overlord)
    self.end.run(debug=debug)

  def goto(self, url):										# Returns Redirect Method to URL
    return redirect(url)

  def form(self, _req=None):							# Returns Requested Form Attribute
    if _req is None:
      return request.form
    return request.form.get(_req)

  def arg(self, _req=None): 							# Returns Requested Argument
    if _req is None:
      return request.args
    return request.args.get(_req)

  def method(self): 											# Returns (GET/POST) Method
    return request.method

  def json(self, to_make):								# Returns Json
    return jsonify(to_make)


""" WEB STRING (reflask.webStr)

  Formats a string to HTML-Friendly-Format
  can be reversed to format HTML strings back
  into ordinary raw strings.
"""


def webStr(to_format, reverse=False):
  # Contains formatting logic
  form = (
    ("'", "&apos;"), (" ", "&nbsp;"),
    ('"', "&quot;"), ("<", "&lt;"),
    (">", "&gt;")
  )
  # Create new value
  new_string = to_format
  # Iterate and replace
  for f in form:
    if reverse:
      new_string.replace(f[1], f[0])
    else:
      new_string.replace(f[0], f[1])
  # Return value
  return new_string
