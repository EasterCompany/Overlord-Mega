# STANDARD LIBRARY IMPORTS
from sys import argv
# ELANG IMPORTS
from modules.elang.reflask import etag, Blueprint
from modules.services.api_manager import service as api_service

# PROJECT APPLICTION
overlord = Blueprint(
  "overlord",
  "overlord",
  template_folder="templates"
)

# APP CONFIGURATION
app = {
  'home': {
    'uri': '/',
    'root': './templates/pages/home.html'
  },
  'epanel': {
    'uri': '/epanel',
    'root': './templates/pages/panel.html'
  },
  'edocs': {
    'uri': '/edocs',
    'root': './templates/pages/home.html'
  },
}


# E DOCUMENT
def serve(name):
  if "@ms" in argv:
    return etag(name)['build']
  if 'app' not in app[name]:
    app[name]['app'] = etag(name)
  return app[name]['app']['build']

# HOME PAGE
@overlord.route(app['home']['uri'])
def home_page():
  return serve(
    app['home']['root']
  )


# E PANEL PAGE
@overlord.route(app['epanel']['uri'])
def epanel_page():
  return serve(
      app['epanel']['root']
    )


# E DOCS PAGE
@overlord.route(app['edocs']['uri'])
def edocs_page():
  return serve(
    app['edocs']['root']
  )


# API BACKEND CALL POINT
@overlord.route('/api', methods=["GET", "POST"])
def _api_distribution_():
  return api_service()

