from __app__ import webApp
from source.elang.edoc import etags, etag, make

ETML = open("./template/app/epanel/epanel.html").read()
FILE = make(name='epanel', etml=ETML)


@webApp.end.route('/epanel', methods=['GET', 'POST'])
def epanel_index():
  return FILE.deploy()

