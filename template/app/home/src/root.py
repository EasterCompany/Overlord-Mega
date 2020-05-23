from __app__ import webApp
from source.elang.edoc import etags, etag, make

ETML = open("./template/app/home/home.html").read()
FILE = make(name='home', etml=ETML)


@webApp.end.route('/', methods=['GET', 'POST'])
def home_index():
  return FILE.deploy()

