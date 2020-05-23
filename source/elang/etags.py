from . import dateTime, sysTime, sysName
from .basic import formatDateTime, git
from .archive import archive
from .server import host
from source import __version__

_g = "./template/global/"

def file(path):
  try:
    return open(path, "r").read()
  except: 
    return ""

def css(css):
  return "<style>" + str(css) + "</style>"

months = [
  '', "Jan", "Feb", "Mar", "Apr", 
  "May", "Jun", "Jul", "Aug", 
  "Sep", "Oct", "Nov", "Dec"
]

def lastMonth():
  m = dateTime.now().month - 1
  if m == 0: return months[-1]
  return months[m]

def getMostHits():
  from __app__ import webApp
  return webApp.mm_hit_count

def getMostReqs():
  from __app__ import webApp
  return webApp.mm_request_count

def getLastHits():
  from __app__ import webApp
  return webApp.lm_hit_count

def getLastReqs():
  from __app__ import webApp
  return webApp.lm_request_count

def getThisHits():
  from __app__ import webApp
  return webApp.tm_hit_count

def getThisReqs():
  from __app__ import webApp
  return webApp.tm_request_count

eTags = {
  
  # test object
  'test': '<!-- pass -->',
  
  # e-doc site defaults
  'site.styles': css(file(_g + "styles/style.css")),
  'site.header': file(_g + "source/header.html"),
  'site.footer': file(_g + "source/footer.html"),
  'site.dexter': file(_g + "script/dexter.js"),
  'site.post': file(_g + "source/elements/post.html"),
  'site.mostHits': getMostHits,
  'site.mostRequests': getMostReqs,
  'site.lastMonthsHits': getLastHits,
  'site.thisMonthsHits': getThisHits,
  'site.lastMonthsRequests': getLastReqs,
  'site.thisMonthsRequests': getThisReqs,
  'host.domain': host.domain,
  'host.host': host.server['host'],
  'host.name': host.server['name'],
  'host.apps': ', '.join(host.server['apps']),
  'host.tables': ', '.join(host.server['tables']),
  
  # e-doc footer objects
  'footer.dexter': file(_g + "source/elements/dexterFooter.html"),
  'footer.edoc': file(_g + "source/elements/edocFooter.html"),
  
  # e-doc css colors
  'color.darkBlue': "#0C0032",
  'color.deepBlue': "#190061",
  'color.blue': "#240090",
  'color.aqua': '#00A0A0',
  'color.green': '#00A000',
  'color.gunMetal': "#282828",
  'color.brownMetal': '#2E1114',
  'color.darkMetal': '#1A1A1D',
  'color.paleMetal': '#4E4E50',
  'color.pinkMetal': '#6F2232',
  'color.redMetal': '#950740',
  'color.red': '#C3073F',
  'color.deepRed': '#501B1D',
  'color.pinkGrey': '#64485C',
  'color.pinkTan': '#83677B',
  'color.titaniumDark': '#A1A1A1',
  'color.titaniumGrey': '#ADADAD',
  'color.titaniumWhite': '#F0F0F0',
  
  # site time functions
  'site.date': str(dateTime.now()).split(' ')[0],
  'site.time': str(dateTime.now()).split(' ')[1],
  'site.date.thisMonth': months[dateTime.now().month],
  'site.sys.name': sysName,
  'site.version': __version__,

  # git repo functions
  'git.readme': git('README.md'),
  
}

hive = archive('test')
hive_record = hive.fetch(0)

def set_hive(*args):
  global hive
  hive = archive(args[0])

def set_hive_record(*args):
  global hive_record
  hive_record = hive.fetch(int(args[0]))

def hive_data(*args):
  if args[0] in hive_record:
    if args[0] == "date":
      if hive_record['date_added'] == hive_record['date_modified']:
        return formatDateTime(hive_record['date_added'])
      else:
        return "Edited: " + formatDateTime(hive_record['date_modified'])
    return hive_record[args[0]]
  return "undefined"

def static_image(*args):
  return "<img src='static/image/" + args[0] + "'>"

def two_bar_graph(*args):
  r = file(_g + "source/elements/statComparison.html").\
    replace('<title!>', args[0]).replace('<subtitle!>', args[1]).\
    replace('<laa!>', args[2]).replace('<lab!>', args[3]).\
    replace('<lba!>', args[4]).replace('<lbb!>', args[5]).\
    replace('<p1!>', args[6]).replace('<p2!>', args[7])
  return r
  
def webAppRequests(*args):
  from __app__ import webApp
  return str(webApp.request_count)

def webAppHits(*args):
  from __app__ import webApp
  return str(webApp.hit_count)

eClasses = {
  'load': set_hive,
  'fetch': set_hive_record,
  'return': hive_data,
  'image': static_image,
  'graph.bar': two_bar_graph,
  'site.requests': webAppRequests,
  'site.hits': webAppHits,
  'site.date.lastMonth': lastMonth,
}

