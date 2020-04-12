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

# PROJECT BACKEND APPLICATIONS
from modules.services.api_manager import service as api_service

# PROJECT FLASK APP & DATABASE
webApp = ReFlask(
    "genesis", 
    react_enabled=False
)
local = "unassigned"


# ======================== WEB APP ROUTE INDEX ========================


""" HOME PAGE (www.easter.company/)

    home page app and page index for
    hosted domain (easter.company) 
    and (eastercompany.co.uk)
"""
@webApp.end.route('/')
def _home_page_():
    return webApp.html_app("home.html")


""" API DISTRIBUTION (.../api)

    capable of distributing api
    services from this domain
"""
@webApp.end.route('/api', methods=["GET", "POST"])
def _api_distribution_():
    return api_service()


# ======================== MAIN.PY _INIT_ FUNC ========================


""" BOOT (__boot__)

    runs the boot functionality
    for eLang & server when installing
    building, hosting or testing
"""
def __boot__():
    global local
    # BOOT REGISTRATION
    if 'secureserver' in uname().node:
        # Host mass.db as main server
        local = Database("mass.db")
        # Mass Database Tables
        imported_tables = [
            client_database_tables,
        ]
    elif 'liveconsole' in uname().node:
        # Host tiny.db as live server
        local = Database("tiny.db")
        # Tiny Databse Tables
        imported_tables = [
            client_database_tables,
        ]
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
    # -- RUN DEBUG MODE --
    if "debug" in argv:
        basic.__unit_test__()
    # -- RUN WEB APP --
    if "start" in argv:
        webApp.run()
