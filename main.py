# -*- coding: utf-8 -*-

# STANDARD LIBRARY IMPORTS
from sys import argv
from datetime import datetime
from platform import uname
from sqlite3 import connect as db_connect

# E-LANG MODULE IMPORTS
from modules.elang import basic
from modules.elang.sqlmem import Database
from modules.elang.reflask import ReFlask, webStr

# PROJECT DATABASE IMPORTS
from modules.database.client_tables import client_database_tables

# ======================== MAIN.PY _INIT_ FUNC ========================


""" BOOT (__boot__)

	runs the boot functionality
	for eLang & server when installing
	building, hosting or testing
"""


def __boot__():
    global local
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
            client_database_tables,
        ]
    for _table in imported_tables:
        for _name, _column in _table:
            local.new_table(_name, _column)
    local.db.commit(), local.db.close()


# INITIALIZATION ON MAIN FILE BOOT
if __name__ == "__main__":

    # -- BOOT WITH USER --
    __boot__()

    # -- APP CONFIGURATION --
    webApp = ReFlask(
        "genesis",
        react_enabled=False
    )
    local = "unassigned"

    # -- RUN DEBUG MODE --
    if "debug" in argv:
        basic.__unit_test__()

    # -- RUN WEB APP --
    if "start" in argv:
        webApp.run()
