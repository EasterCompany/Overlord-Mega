from . import path, deformat, pyArgs
from .reflask import app
from .etags import eTags


# Convert value to web string (or reverse)
def txt(to_format, reverse=True):
  form = (
  ("'", "&apos;"), (" ", "&nbsp;"),
  ('"', "&quot;"), ("<", "&lt;"),
  (">", "&gt;"), ("`", "&#96;")
  )
  new_string = str(to_format)
  for f in form:
    if reverse:
      new_string = new_string.replace(f[1], f[0])
    else:
      new_string = new_string.replace(f[0], f[1])
  return new_string


# Returns value as e-tag
def E(string=''):
  return deformat("<! " + str(string) + " !>")


# Finds etags within content
def etags(content):
  tags, content = [], deformat(content)
  if "<!" in content:
    content = content.split("<!")
  for tag in content:
    if "!>" in tag:
      t = tag.split("!>")[0]
      if t not in tags:
        tags.append(t)
  return tags


# Finds & Replaces etags with content
def etag(content):
  tags = etags(content)
  content = content \
    .replace('<! ', '<!') \
    .replace(' !>', '!>')
  for tag in tags:
    if tag in eTags:
      replacement = eTags[tag]
      if callable(replacement):
        replacement = replacement()
      content = content.replace(E(tag), etag(replacement))
  return content


class make:

  def __init__(self, name, etml='', style='', script=''):
    self.name, self.etml, self.script, self.style = \
      name, etml, script, style
    self.create(name, etml, style, script)

  def create(self, name, etml, style, script):
    ejs_root_file = "./template/app/" + str(name) + "/" + str(name) + ".js"
    etg_root_file = "./template/app/" + str(name) + "/" + str(name) + ".html"
    self.doc = {
      'name': str(name),
      'etml': str(etml),
      'style': str(open('./template/global/styles/style.css').read()) + str(style),
      'script': str(open('./template/global/script/dexter.js').read()) + str(script),
      'app': app(str(name), str(name), sub=True),
      'file': etg_root_file,
    }
    if path.exists(ejs_root_file) \
      and not path.exists(etg_root_file):
      self.doc['file'] = open(ejs_root_file).read()
    else:
      self.doc['file'] = open(etg_root_file).read()

  def render(self):
    ess = etag(self.doc['style'])
    etml = etag(self.doc['etml'])
    ejs = etag(self.doc['script'])
    self.doc['build'] = \
      deformat(
        """<!DOCTYPE html>
        <style>
          <! .css !>
        </style>
        <html>
          <! .html !>
        </html>
        <script>
          <! .js !>
        </script>
        """ . \
        replace("<! .css !>", ess) . \
        replace("<! .html !>", etml) . \
        replace("<! .js !>", ejs),
        remove_white_space=False
      )
    return self.doc

  def run(self):
    self.render()
    return self.doc['build']

  def deploy(self):
    if '-t' in pyArgs or 'test' in pyArgs:
      self.create(self.name, self.etml, self.style, self.script)
      self.render()
    return self.doc['build']

