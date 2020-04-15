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
    # SECURE SERVER (EU SERVER)
    if 'secureserver' in uname().node:
        # Host mass.db as main server
        local = Database("mass.db")
        # Mass Database Tables
        imported_tables = [
            client_database_tables,
        ]

    # LIVE CONSOLE (NA SERVER)
    elif 'liveconsole' in uname().node:
        # Host tiny.db as live server
        local = Database("tiny.db")
        # Tiny Databse Tables
        imported_tables = [
            client_database_tables,
        ]

    # LOCAL SYSTEMS
    else:
        # Set default .local database
        local = Database("data.db")
        # Local Database Tables
        imported_tables = [
            client_database_tables,
        ]

    # MAKE TABLES THAT DON'T EXIST
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
