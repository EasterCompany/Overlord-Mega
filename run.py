# STANDARD LIBRARY IMPORTS ---
from os.path import dirname
from sys import argv, path
from platform import uname

# PROJECT IMPORTS --------------
from modules.elang.sqlmem import Database
from modules.elang.reflask import ReFlask
from modules.elang.this import this

# PROJECT PAGE INDEX IMPORTS ---
from templates.pages.home.home import home_app
from templates.pages.error.error import error_app

# PROJECT DATABASE IMPORTS -----
from modules.database import client

# ~~~~ DEFINE SYSTEM SPECIFICS ~~~~
if 'secureserver' in uname().node:
  local = Database("mass.db")
  imported_tables = [
    client.tables,
  ]
  hosted_apps = [
    home_app,
  ]

elif 'liveconsole' in uname().node:
  local = Database("tiny.db")
  imported_tables = [
    client.tables,
  ]  
  hosted_apps = [
    home_app,
    error_app,
  ]

else:
  local = Database("data.db")
  imported_tables = [
  ]
  hosted_apps = [
    home_app,
    error_app,
  ]

# DATABASE REGISTRATION
for _table in imported_tables:
  for _name, _column in _table:
    local.new_table(_name, _column)
local.db.commit(), local.db.close()

# SERVER REGISTRATION
path.insert(0, dirname(__file__))
webapp = ReFlask()

# ~~~~ DEFINE APP ROUTE INDEX ~~~~
for app in hosted_apps:
  webapp.end.register_blueprint(app)

# LOCAL SERVER BOOT REGISTRATION
if __name__ == "__main__" and len(argv) > 1:
  if ("-t" in argv) or ("test" in argv):
    webapp.run(debug=True)
  if ("-s" in argv) or ("start" in argv):
    webapp.run()
