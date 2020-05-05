from .basic import exists
from .reflask import app


class e:

  def __init__(self, name, etml='', style='', script=''):
    self.doc = {
      'name': name,
      'etml': str(etml),
      'style': str(open('./templates/site/styles/style.css').read()) + str(style),
      'script': str(open('./templates/site/scripts/dex.js').read()) + str(script),
      'app': app(name, name),
      'build': None,
      'ejs': None,
      'file': "./templates/pages/" + name + "/app.js",
    }
    print(self.doc)

  def render(self):
    if exists("./templates/pages/" + self.doc['name'] + "/app.js"):
      self.doc['ejs'] = open(self.doc['file']).read()
    else:
      self.doc['ejs'] = None
    self.edoc['build'] = \
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
      replace("<! .css !>", self.doc['style']). \
      replace("<! .html !>", self.doc['etml']). \
      replace("<! .js !>", self.doc['script'])
    return self.doc

  def run(self):
    self.render()
    return self.doc['build']
