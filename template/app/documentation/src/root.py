
from __app__ import webApp
from source.elang.edoc import etags, etag, make

ETML = open("./template/app/documentation/documentation.html").read()
FILE = make(name='documentation', etml=ETML)
RNDR = FILE.render()


@webApp.end.route('/documentation', methods=['GET', 'POST'])
def documentation_index():
  return FILE.deploy()


