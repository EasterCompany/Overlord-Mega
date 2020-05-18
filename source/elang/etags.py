from . import dateTime, sysTime

_g = "./template/global/"

def file(path):
  return open(path, "r").read()

def css(css):
  return "<style>" + str(css) + "</style>"

def formatDateTime(datetime=dateTime.now()):
  date, time = \
    str(dateTime.now()).split(' ')[0], str(dateTime.now()).split(' ')[1]
  _Date, _Time = \
    str(datetime).split(' ')[0], str(datetime).split(' ')[1]
  if date == _Date:
    hours = int(_Time.split(':')[0]) - int(time.split(':')[0])
    if hours >= 2:
      return str(hours) + " hours ago"
    elif hours == 1:
      return str(hours) + " hour ago"
    else:
      return "minutes ago"  
  else:
    return _Date

eTags = {
  # Test object
  'test': '<!-- pass -->',
  # e-doc site defaults
  'site.styles': css(file(_g + "styles/style.css")),
  'site.header': file(_g + "source/header.html"),
  'site.footer': file(_g + "source/footer.html"),
  'site.dexter': file(_g + "script/dexter.js"),
  # e-doc footer objects
  'footer.dexter': file(_g + "source/elements/dexterFooter.html"),
  'footer.edoc': file(_g + "source/elements/edocFooter.html"),
  # e-doc css colors
  'color.darkBlue': "#0C0032",
  'color.deepBlue': "#190061",
  'color.blue': "#240090",
  'color.skyBlue': "#3500D3",
  'color.gunMetal': "#282828",
  'color.brownMetal': '#2E1114',
  'color.darkMetal': '#1A1A1D',
  'color.paleMetal': '#4E4E50',
  'color.pinkMetal': '#6F2232',
  'color.rose': '#950740',
  'color.rouge': '#C3073F',
  'color.deepRose': '#501B1D',
  'color.pinkGrey': '#64485C',
  'color.pinkTan': '#83677B',
  'color.titanium': '#ADADAD',
  'site.date': str(dateTime.now()).split(' ')[0],
  'site.time': str(dateTime.now()).split(' ')[1],
  'site.datetime': str(formatDateTime())
}