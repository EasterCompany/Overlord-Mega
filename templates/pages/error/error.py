# REQUIRED APP MODULES
from modules.elang.reflask import Blueprint, etag

# TEMPLATE HEADER
app = Blueprint("error", "overlord")
doc = etag('./templates/pages/error/error.html')

# APP ROUTE & FUNCTION
@app.route('/displayerror')
def error_page():
  return doc['build']
