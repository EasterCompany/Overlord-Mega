# REQUIRED APP MODULES
from modules.elang.reflask import Blueprint

# TEMPLATE HEADER
error_app = Blueprint("error", "overlord")
error_eDoc = "etag('./templates/pages/error/errorPage.js', 'error.html')"

# APP ROUTE & FUNCTION
@error_app.route('/displayerror')
def __error_page_backend__():
  return "error_eDoc['build']"
