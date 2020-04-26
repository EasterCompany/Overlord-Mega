# REQUIRED APP MODULES
from modules.elang.reflask import Blueprint, etag

# TEMPLATE HEADER
app = Blueprint("home", "overlord")
doc = etag('./templates/pages/home/home.html')

# APP ROUTE & FUNCTION
@app.route('/')
def home_page():
  return doc['build']
