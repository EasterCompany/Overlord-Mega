from . import dateTime, sysTime
from .basic import formatDateTime, git
from .archive import archive

_g = "./template/global/"


def file(path):
  return open(path, "r").read()


def css(css):
  return "<style>" + str(css) + "</style>"


eTags = {
  
  # test object
  'test': '<!-- pass -->',
  
  # e-doc site defaults
  'site.styles': css(file(_g + "styles/style.css")),
  'site.header': file(_g + "source/header.html"),
  'site.footer': file(_g + "source/footer.html"),
  'site.dexter': file(_g + "script/dexter.js"),
  'site.post': file(_g + "source/elements/post.html"),
  
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

  # git repo functions
  'git.readme': git('README.md'),
  
}

hive = archive('test')
hive_record = hive.fetch(0)

def set_hive(arc):
  global hive
  hive = archive(arc)

def set_hive_record(_id):
  global hive_record
  hive_record = hive.fetch(int(_id))

def hive_data(data):
  if data in hive_record:
    if data == "date":
      if hive_record['date_added'] == hive_record['date_modified']:
        return formatDateTime(hive_record['date_added'])
      else:
        return "Edited: " + formatDateTime(hive_record['date_modified'])
    return hive_record[data]
  return "undefined"

def static_image(path):
  return "<img src='static/image/" + path + "'>"

eClasses = {
  'load': set_hive,
  'fetch': set_hive_record,
  'return': hive_data,
  'image': static_image,
}

