from . import \
  mkDir, chDir, workDir, \
  console, path, sysName, pyArgs
from flask import \
  Flask, Blueprint, \
  redirect, request, jsonify
from .server import host
from .comrade import comrade
from source import __version__


class app:
  default_sub_apps = host.server['apps']
  request_count = 0
  hit_count = 0
  lm_request_count = 0
  lm_hit_count = 0
  tm_request_count = 0
  tm_hit_count = 0
  mm_request_count = 0
  mm_hit_count = 0
  end = None

  def __init__(self, name=__name__, react_enabled=False, sub=True):
    self.nme = name
    self.cwd = workDir()
    self.debug = False
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
      f = open('./__app__.py', 'w+')
      r = f.read()
      r = '''"""   MAIN PYTHON IMPORT FILE FOR APP   """
from source.elang.reflask import __mainWebApp__ as webApp'''
      for default in self.default_sub_apps:
        self.has_app(default)
        py_import = "\nfrom template.app." + default + ".src import root as _APP_" + default.upper() + "_"
        r += py_import
      r += '\n""" /                                     / """'
      f.write(r), f.close()
    
    @self.end.before_request
    def _count_global_request():
      comrade.mass_update("cReqs", int(self.request_count) + 1)
      comrade.mass_update("cHits", int(self.hit_count) + 1)

  def run(self):
    self.debug = ("-t" in pyArgs or "test" in pyArgs)
    self.end.run(debug=self.debug, port=3001)

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
    mkDir(self.cwd + "/template/app/" + app_name + "/src")
    html_root_file = self.cwd + "/template/app/" + app_name + "/" + app_name + ".html"
    py_root_file = self.cwd + "/template/app/" + app_name + "/src/root.py"
    if not path.exists(html_root_file):
      f = open(html_root_file, 'w')
      f.write(
"""<! site.header !>

<body class="content">
    <img
      class="post-banner" 
      src="/static/icon/ms-icon-310x310.png">
    <h3 class="redline"> Untitled </h3>
    <h5>development in progress...</h5>
    <p>
      Congratulations on cloning and installing elang & edocs!<br>
      <br>
      If you get stuck you can check the docs here within your app; or over at <a href="http://github.com/EasterCompany">github</a>
    </p>
</body>

<! site.footer !>
""")
      f.close()
    if not path.exists(py_root_file):
      f = open(py_root_file, 'w')
      f.write(
"""from __app__ import webApp
from source.elang.edoc import etags, etag, make

ETML = open("./template/app/""" + app_name + "/" + app_name + """.html").read()
FILE = make(name='""" + app_name + """', etml=ETML)


@webApp.end.route('/""" + app_name + """', methods=['GET', 'POST'])
def """ + app_name + """_index():
  return FILE.deploy()

"""   )
      f.close()


__mainWebApp__ = app(name=sysName, react_enabled=False, sub=False)

