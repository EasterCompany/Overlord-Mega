
from __app__ import webApp
from source.elang.edoc import etags, etag, make

ETML = open("./template/app/error/error.html").read()
FILE = make(name='error', etml=ETML)
RNDR = FILE.render()


@webApp.end.route('/error', methods=['GET', 'POST'])
def error_index():
  return FILE.deploy()


