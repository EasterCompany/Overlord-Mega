from . import path, console, sysName, client, strColor


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
        "home", "error"
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
        "home", "error"
      ],
      'tables': []
    },

    "system": {
      'ssl': False,
      'name': 'localhost',
      'path': aliases[0],
      'port': 3001,
      'host': 'http://secure.easter.company/',
      'apps': [
        "home", "error"
      ],
      'tables': []
    }

  }
  server = servers['system']

  def __init__(self):
    self.server = self.specifiedServer()

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

  def isSecureServer(self):
    return 'secureserver' in sysName

  def isStableServer(self):
    return 'liveconsole' in sysName

  def isLocalServer(self):
    if not self.isSecureServer() and not self.isStableServer():
      return True
    return False

  def consoleLog(self):
    return print(
      """
      """ + strColor.green('elang.server') + """
       """ + strColor.blue('NAME :'), str(self.domain) + """
       """ + strColor.blue('APPS :'), str(', '.join(self.server['apps'])),"""
       """ + strColor.blue('TEST :'), str(self.url()) + """
       """ + strColor.blue('LIVE :'), str(self.server['host']) , """
      """
    )

server = __this__()
