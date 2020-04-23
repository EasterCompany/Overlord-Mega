# STANDARD LIBRARY IMPORTS ---
from os.path import dirname
from sys import argv, path
from platform import uname

# ELANG IMPORTs --------------
from modules.elang.sqlmem import Database
from modules.elang.reflask import ReFlask

# PROJECT DATABASE IMPORTS ---
from modules.database.client_tables import client_database_tables

# ~~~~ DEFINE TABLES ON BOOT ~~~~
if 'secureserver' in uname().node:
    local = Database("mass.db")
    imported_tables = [
        client_database_tables,
    ]
elif 'liveconsole' in uname().node:
    local = Database("tiny.db")
    imported_tables = [
        client_database_tables,
    ]
else:
    local = Database("data.db")
    imported_tables = [
    ]
for _table in imported_tables:
    for _name, _column in _table:
        local.new_table(_name, _column)
local.db.commit(), local.db.close()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# SERVER REGISTRATION
path.insert(0, dirname(__file__))
application = ReFlask()

# LOCAL SERVER BOOT REGISTRATION
if __name__ == "__main__" and "@ms" in argv:
    if ("d" in argv) or ("debug" in argv):
        from modules.elang import basic
        basic.__unit_test__()
    if ("r" in argv) or ("run" in argv) or ("start" in argv):
        application.run()
