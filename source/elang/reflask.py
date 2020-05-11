from . import \
  mkDir, chDir, workDir, \
  console, pyArgs, path
from flask import \
  Flask, Blueprint, \
  redirect, request, jsonify


class app:
  default_sub_apps = [
    'error', 'api'
  ]

  def __init__(self, name=__name__, react_enabled=False, sub=False):
    self.nme = name
    self.cwd = workDir()
    if sub:
      self.end = Blueprint(name, name, self.cwd + '/static', '/static')
    else:
      mkDir("./public")             # PUBLIC Information
      mkDir("./static/build")       # LOCAL eDoc build files
      mkDir("./static/icon")        # LOCAL icon files
      mkDir("./static/image")       # LOCAL image files
      mkDir("./template/global/script")
      mkDir("./template/global/source")
      mkDir("./template/global/styles")
      mkDir("./template/global/themes")
      mkDir("./template/app")       # APP HTML/CSS/JS Templates
      self.end = Flask(name)
      if "build" in pyArgs:
        if react_enabled:
          mkDir("./static/react")
          chDir("apps/" + name)
          console("npm run build")
          chDir(self.rwd)
    for default in self.default_sub_apps:
      self.has_app(default)

  def run(self, debug=False):
    self.end.run(debug=debug)

  def goto(self, url):
    return redirect(url)

  def form(self, _req=None):
    if _req is None:
      return request.form
    return request.form.get(_req)

  def arg(self, _req=None):
    if _req is None:
      return request.args
    return request.args.get(_req)

  def method(self):
    return request.method

  def json(self, to_make):
    return jsonify(to_make)

  def has_app(self, app_name):
    mkDir(self.cwd + "/template/app/" + app_name + "/scripts")
    root_file = self.cwd + "/template/app/" + app_name + "/" + app_name + ".html"
    if not path.exists(root_file):
      return open(root_file, 'w').read()
    else:
      return open(root_file).read()
