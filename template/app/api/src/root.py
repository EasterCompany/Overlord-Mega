from __app__ import webApp
from source.elang.basic import crypt
from source.elang.comrade import comrade, com_api_map_reqest, com_api_request


@webApp.end.route('/api', methods=['GET', 'POST'])
def api_index():
  _decrypt = crypt().de
  args = webApp.arg()
  
  def deCode(arg):
    return bytes(
      str(
        arg
      ).encode('utf-8')
    ).decode('utf-8') + "=="
  
  def decrypt(arg):
    return bytes(
      _decrypt(
        bytes(
          arg.encode('utf-8')
        )
      )
    ).decode('utf-8')
  
  # API PARAMETER ORDER
  api = bytes(str(webApp.arg('req')).encode('utf-8'))
  api = _decrypt(api).decode('utf-8')
  
  # API SET VARIABLE 
  def values(args=args):
    vs = []
    for arg in args:
      if arg == "req":
        pass
      else:
        vs.append(
          decrypt(
            deCode(
              arg
            )
          )
        )
    return vs
  v = values()
  
  if api == "cMap":
    return webApp.json(com_api_map_reqest())

  elif api == "cShare":
    comrade.share(str(v[0]), str(v[1]), str(v[2]))
  
  elif api == "cHits":
    return comrade.get("cHits")

  elif api == "cReqs":
    return comrade.get("cReqs")
  
  return webApp.json({ 'status': 1 })

