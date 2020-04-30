# REQUIRED APP MODULES
from modules.elang.reflask import Blueprint

# TEMPLATE HEADER
home_app = Blueprint("home", "overlord")
home_eDoc = "etag(content='./templates/pages/home/homePage.js', name='index.html')"

# APP ROUTE & FUNCTION
@home_app.route('/')
def __home_app_backend__():
  return "home_eDoc['build']"
