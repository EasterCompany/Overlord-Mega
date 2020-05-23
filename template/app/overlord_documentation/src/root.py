
from __app__ import webApp
from source.elang.edoc import etags, etag, make

ETML = open("./template/app/overlord_documentation/overlord_documentation.html").read()
FILE = make(name='overlord_documentation', etml=ETML)


@webApp.end.route('/overlord_documentation', methods=['GET', 'POST'])
def overlord_documentation_index():
  return FILE.deploy()


