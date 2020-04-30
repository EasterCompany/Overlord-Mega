# -*- coding: utf-8 -*-

# STANDARD LIBRARY IMPORTS
from os import system, chdir, getcwd, walk
from os.path import realpath
from sys import platform, argv, executable
from sqlite3 import connect
# THIRD-PARTY IMPORTS
from flask import Flask, render_template, redirect, request, jsonify, Blueprint
# INTERNAL IMPORTS
from modules.elang.basic import make_path, deformat, listReplace


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


""" ETAGS (basic.etags)

  fetches and returns etags
  found within string or list
  of strings.
"""


def etags(content):
  tags, content = [], deformat(content)
  if "<!" in content:
    content = content.split("<!")
    for index, tag in enumerate(content):
      if "!>" in tag:
        tags.append(tag.split("!>")[0])
  else:
    return None
  return tags


def E(string):
  return "<!" + string + "!>"


""" ejs language tag openers """
def _ejs_tag_openers(type):
    return [
        "<" + type + "{", 
        "< " + type + "{", 
        "< " + type + " {",
        "<" + type + " {"
        ]


""" ejs language tag openers """
def _ejs_tag_closers(type):
    return [
        "}" + type + ">", 
        "} " + type + ">", 
        "} " + type + " >",
        "}" + type + " >"
        ]
    

""" ejs language tags """
def ejs_language_tags():
  css = _ejs_tag_openers("css")
  html = _ejs_tag_openers("html")
  js = _ejs_tag_openers("javascript")
  return css + html + js


""" ETAG (basic.etag)
  converts eTags into file contents
  if passing a directory as a parameter
  make sure to use "./" and only pass
  files contained within the working dir
"""


def etag(content, name='untitled'):
  
  # OPEN ETAG-ED FILE
  def etagDoc(document_containing_etags):
    return deformat(open(document_containing_etags).read())
  
  # GET LOCAL TAGGABLE CONTENT
  def localTags(_type):
    for (dirpath, dirnames, filenames) in walk("./templates/site/" + _type):
      _local = filenames
      break
    for index, theme in enumerate(_local):
      if _type == "styles" or _type == "themes":
        file_type = "css"
      elif _type == "scripts":
        file_type = "js"
      elif _type == "docs":
        file_type = "html"
      else: 
        return None
      if _local[index].endswith("." + file_type):
        _local[index] = [
          "eDoc." + _local[index].split('.')[0], 
          etagDoc("./templates/site/" + _type + "/" + _local[index])]  
    return _local
  
  # DEFINE ELANG OPTIONS
  _build_file_ = open('./static/build/' + name, "w+")
  _compiled_script_ = open(content).read()
  _script_has_tags = True
  for tag in ejs_language_tags():
    if tag in _compiled_script_:
      break
    _script_has_tags = False
  if _script_has_tags:
        _compiled_script_ = "<script>" + _compiled_script_ + "</script>"
  else:
    for tag in _ejs_tag_openers("css"):
      _compiled_script_ = _compiled_script_.replace(tag, "<style>")
    for tag in _ejs_tag_closers("css"):
      _compiled_script_ = _compiled_script_.replace(tag, "</style>")
    for tag in _ejs_tag_openers("html"):
      _compiled_script_ = _compiled_script_.replace(tag, "<html>")
    for tag in _ejs_tag_closers("html"):
      _compiled_script_ = _compiled_script_.replace(tag, "</html>")
    for tag in _ejs_tag_openers("javascript"):
      _compiled_script_ = _compiled_script_.replace(tag, "<script>")
    for tag in _ejs_tag_closers("javascript"):
      _compiled_script_ = _compiled_script_.replace(tag, "</script>")
  
  eDoc = {
    'name': name,
    'tags': None,
    'front': _compiled_script_,
    'header': etagDoc("./templates/site/docs/header.html"),
    'footer': etagDoc("./templates/site/docs/footer.html"),
    'styles': localTags('styles'),
    'themes': localTags('themes'),
    'scripts': localTags('scripts'),
    'build': None
  }
  
  # MAKE BUILD FILE FOR E-DOCUMENT
  _build_file_.write("<!DOCTYPE html>\n<header>" + eDoc['header'] + "</header>\n\n<style>\n")
  for style in eDoc['styles']:
    _build_file_.write(style[1])
  _build_file_.write("\n</style>\n\n" + eDoc['front'] + "\n\n<script>\n")
  for script in eDoc['scripts']:
    _build_file_.write(script[1])
  _build_file_.write("\n</script>\n\n" + eDoc['footer'])
  _build_file_.close()
  eDoc['build'] = deformat(open('./static/build/' + name).read())
  
  # RETURN DOCUMENT DICTIONARY OBJECT
  return eDoc


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
      make_path("./public")     # PUBLIC Information
      make_path("./static")     # STATIC DIRECTORY
      make_path("./static/build")   # local eDoc build files
      make_path("./static/icon")    # local icon files
      make_path("./static/image")   # local image files
      make_path("./templates")      # TEMPLATES DIRECTORY
      make_path("./templates/site")     # HTML/CSS/JS Objects
      make_path("./templates/pages")    # HTML/CSS/JS Templates
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
