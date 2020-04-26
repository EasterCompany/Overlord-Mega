# STANDARD LIBRARY IMPORTS ---
from os.path import dirname
from sys import argv, path
from platform import uname

# PROJECT IMPORTS --------------
from modules.elang.sqlmem import Database
from modules.elang.reflask import ReFlask

# PROJECT PAGE INDEX IMPORTS ---
from templates.pages.home import home
from templates.pages.error import error

# PROJECT DATABASE IMPORTS -----
from modules.database.client_tables import client_database_tables

# ~~~~ DEFINE SYSTEM SPECIFICS ~~~~
if 'secureserver' in uname().node:
  local = Database("mass.db")
  imported_tables = [
    client_database_tables,
  ]
  hosted_apps = [
    home.app,
    error.app,
  ]
elif 'liveconsole' in uname().node:
  local = Database("tiny.db")
  imported_tables = [
    client_database_tables,
  ]
  hosted_apps = [
    home.app,
    error.app,
  ]
else:
  local = Database("data.db")
  imported_tables = [
  ]
  hosted_apps = [
    home.app,
    error.app,
  ]

# DATABASE REGISTRATION
for _table in imported_tables:
  for _name, _column in _table:
    local.new_table(_name, _column)
local.db.commit(), local.db.close()

# SERVER REGISTRATION
path.insert(0, dirname(__file__))
application = ReFlask()

# ~~~~ DEFINE APP ROUTE INDEX ~~~~
for app in hosted_apps:
  application.end.register_blueprint(app)

# LOCAL SERVER BOOT REGISTRATION
if __name__ == "__main__" and "@ms" in argv:
  if ("t" in argv) or ("test" in argv):
    from modules.elang.basic import __unit_test__
    __unit_test__(), application.run(debug=True)
  elif ("s" in argv) or ("start" in argv):
    application.run()
