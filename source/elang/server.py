from . import path, console, sysName, \
  strColor, sysPath, openUrl, pyArgs
from source.elang.schema import client
from source.elang.basic import crypt


class __this__:
  domain = "easter.company"
  aliases = [ ':', 'eastercompany.co.uk' ]
  servers = {

    "secure": {
      'ssl': False,
      'name': 'secure.',
      'path': domain,
      'port': '/',
      'host': None,
      'apps': [
        "home", "error", "api", 
        "overlord_documentation", "epanel"
      ],
      'tables': [
        client.tables,
      ]
    },

    "stable": {
      'ssl': True,
      'name': 'www.',
      'path': domain,
      'port': '/',
      'host': 'http://secure.easter.company/',
      'apps': [
        "home", "error", "api", 
        "overlord_documentation", "epanel"
      ],
      'tables': []
    },

    "system": {
      'ssl': False,
      'name': 'localhost',
      'path': aliases[0],
      'port': '3001/',
      'host': 'http://secure.easter.company/',
      'apps': [
        "home", "error", "api", 
        "overlord_documentation", "epanel"
      ],
      'tables': []
    }

  }
  server = servers['system']
  stats = [
    "cReqs", 
    "cHits", "clmReqs", 
    "clmHits", "ctmReqs", 
    "ctmHits", "cmmReqs", 
    "cmmHits"
  ]

  def __init__(self):
    self.server = self.specifiedServer()
    sysPath.insert(0, path.dirname(__file__))
    self.consoleLog()

  def sourceableApps(self):
    source = []
    no_source = []
    for page in self.server['apps']:
      if path.exists("./template/app/" + page):
        source.append(page)
      else:
        no_source.append(page)
    return {
      'source': source,
      'no-source': no_source,
      }

  def specifiedServer(self):
    if self.isSecureServer(): return self.servers["secure"]
    elif self.isStableServer(): return self.servers["stable"]
    elif self.isLocalServer(): return self.servers["system"]

  def sslEnabled(self):
    return self.server['ssl']

  def url(self):
    if self.server['ssl']:
      http = 'https://'
    else:
      http = 'http://'
    return http + self.server['name'] + self.server['path'] + str(self.server['port'])

  def hasNoMaster(self):
    return self.server['host'] is None

  def isSecureServer(self):
    return 'secureserver' in sysName or '-t' in pyArgs or 'test' in pyArgs

  def isStableServer(self):
    return 'liveconsole' in sysName

  def isLocalServer(self):
    if not self.isSecureServer() and not self.isStableServer():
      return True
    return False

  def ssl(self, b):
    if b: return 'https://'
    return 'http://'
  
  def consoleLog(self):
    return print(
      """
      """ + strColor.green('elang.server') + """
       """ + strColor.blue('NAME :'), str(self.domain) + """
       """ + strColor.blue('APPS :'), str(', '.join(self.server['apps'])),"""
       """ + strColor.blue('TEST :'), str(self.url()) + """
       """ + strColor.blue('LIVE :'), self.ssl(self.servers['stable']['ssl']) + self.servers['stable']['name'] +
        self.servers['stable']['path'] +
        str(self.servers['stable']['port']), """
      """
    )


host = __this__()
host_crypt = crypt()


def api(service, args):
  _host = host.server['host']
  service = host_crypt.en(service).decode('utf-8')
  parameters = []
  for i, a in enumerate(args):
    parameters.append(host_crypt.en(a).decode('utf-8'))
  try:
    return openUrl(_host + 'api?req=' + service + "&".join(parameters))
  except Exception as error:
    if str(error) == "<urlopen error [Errno -2] Name or service not known>":
      return ""
