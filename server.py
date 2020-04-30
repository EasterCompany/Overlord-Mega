# STANDARD LIBRARY IMPORTS ---
from os.path import dirname
from sys import argv, path
from platform import uname

# PROJECT IMPORTS --------------
from modules.elang.sqlmem import Database
from modules.elang.reflask import ReFlask

# PROJECT PAGE INDEX IMPORTS ---
from templates.pages.home.home import home_app
from templates.pages.error.error import error_app

# PROJECT DATABASE IMPORTS -----
from modules.database.client_tables import client_database_tables

# ~~~~ DEFINE SYSTEM SPECIFICS ~~~~
if 'secureserver' in uname().node:
  local = Database("mass.db")
  # TABLES TO RECORD ON EU SERVER (C-PANEL)
  imported_tables = [
    client_database_tables,
  ]
  # APPS TO HOST ON EU SERVER (C-PANEL)
  hosted_apps = [
    home_app,
  ]

elif 'liveconsole' in uname().node:
  local = Database("tiny.db")
  # TABLES TO RECORD ON NA SERVER (LIVE CONSOLE)
  imported_tables = [
    client_database_tables,
  ]  
  # APPS TO HOST ON NA SERVER (LIVE CONSOLE)
  hosted_apps = [
    home_app,
    error_app,
  ]
else:
  local = Database("data.db")
  # TABLES TO RECORD ON USER.LOCAL
  imported_tables = [
  ]
  # APPS TO HOST ON LOCALHOST
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
if __name__ == "__main__" and "@ms" in argv:
  if ("t" in argv) or ("test" in argv):
    from modules.elang.basic import __unit_test__
    __unit_test__()
  elif ("s" in argv) or ("start" in argv):
    webapp.run()
