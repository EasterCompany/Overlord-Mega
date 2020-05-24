from passenger_wsgi import webApp
from source.elang.comrade import comrade
from source.elang.edoc import etags, etag, make

ETML = open("./template/app/epanel/epanel.html").read()
FILE = make(name='epanel', etml=ETML)


@webApp.end.route('/epanel', methods=['GET', 'POST'])
def epanel_index():
  return FILE.deploy()


def prepRaidData(Req, Hit, REQ, HIT):
  # create requests / hits record
  if not comrade.exists(Req) or not comrade.exists(Hit):
    REQ, HIT = 0, 0
    comrade.share(Req, REQ)
    comrade.share(Hit, HIT)
  # fetch request and hit data from master
  REQ = comrade.get(Hit, True)
  HIT = comrade.get(Req, True)
  # error correct result
  if REQ == "": REQ = 0
  if HIT == "": HIT = 0
  return REQ, HIT


prepRaidData("cReqs", "cHits", webApp.request_count, webApp.hit_count)
prepRaidData("clmReqs", "clmHits", webApp.lm_request_count, webApp.lm_hit_count)
prepRaidData("ctmReqs", "ctmHits", webApp.tm_request_count, webApp.tm_hit_count)
prepRaidData("cmmReqs", "cmmHits", webApp.mm_request_count, webApp.mm_hit_count)
