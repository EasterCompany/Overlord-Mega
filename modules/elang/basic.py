# -*- coding: utf-8 -*-

# Standard library imports
from os import mkdir, system
from os.path import exists, realpath
from platform import uname
from sys import executable, argv
from urllib.request import urlopen


# ======================= EASTER LANGUAGE BASIC SUITE ==========================


""" install support modules

  installs supported third-party
  modules that may be essential
  to basic functionality. 
  TO DO: ADD OFFLINE SUPPORT
"""


def _install_support_modules(_run_tests=False, *args):
  try:
    if _run_tests:
      from flask import Flask
    else:
      system(realpath(executable) + " -m pip install --upgrade pip")
      system(realpath(executable) + " -m pip install --upgrade flask")
    return True
  except Exception as e:
    return e


if ("-i" in argv or "-install" in argv) and (exists("./.git")):
  _install_support_modules()
  system("git pull")


""" DE-FORMAT """


def deformat(string, remove_white_space=False):
  if remove_white_space:
    string = string.replace(" ", "")
  else:
    while "  " in string:
      string = string.replace("  ", " ")
  return string.\
    replace("<! ", "<!").replace(" !>", "!>").\
    replace("\n", "").replace("\r", "").\
    replace("\t", "").replace("\v", "").\
    replace("> <", "><")


""" replace x, and y with r in z """
def listReplace(c, l, r):
  for x in l: 
    c = c.replace(x, r)
  return c


""" MAKE PATH (basic.make_path)

  capable of creating a list
  of directories of embedding
  a new directory within other
  direcotories which may not
  exist.
"""


def make_path(path_to_make, return_path=False):
  p = path_to_make.split('/')
  for i in enumerate(p):
    current_path, j = "", 0
    while j <= i[0]:
      current_path, j = current_path + p[j] + '/', j + 1
    if not exists(current_path):
      mkdir(current_path)
  if return_path:
    return path_to_make
  return exists(path_to_make)


""" git (basic.git)

  returns contents of a
  raw.githubusercontent
  repo file
"""


def git(file_path, repo="Overlord", branch="master", source="EasterCompany"):
  try:
    return urlopen("https://raw.githubusercontent.com/" +
             source + "/" + repo + "/" + branch + "/" + file_path).read().decode('utf-8')
  except Exception as error:
    return error


""" String With Colour (basic.StringWithColour)

  returns a string surrounded by
  BASH / BATCH colour code tags
"""


class StringWithColour:
  content = None
  endOfString = '\033[0m'

  def __init__(self, as_string_with_colour=""):
    self.content = str(as_string_with_colour)

  def _string_(self, string=""):
    if self.content is not None:
      return str(self.content)
    return string

  def white(self, string=""):
    return '\033[97m' + self._string_(string) + self.endOfString

  def blue(self, string=""):
    return '\033[96m' + self._string_(string) + self.endOfString

  def pink(self, string=""):
    return '\033[95m' + self._string_(string) + self.endOfString

  def purple(self, string=""):
    return '\033[94m' + self._string_(string) + self.endOfString

  def yellow(self, string=""):
    return '\033[93m' + self._string_(string) + self.endOfString

  def green(self, string=""):
    return '\033[92m' + self._string_(string) + self.endOfString

  def red(self, string=""):
    return '\033[91m' + self._string_(string) + self.endOfString

