# -*- coding: utf-8 -*-

# STANDARD LIBRARY IMPORTS
from sys import argv
from datetime import datetime
from sqlite3 import connect as db_connect

# EASTER LANGUAGE IMPORTS
from modules.elang import basic
from modules.elang.sqlmem import Database
from modules.elang.reflask import ReFlask, webStr

# PROJECT DATABASE IMPORTS 
from modules.database.client_tables import client_database_tables

# PROJECT BACKEND APPLICATIONS
from modules.services.api_manager import service as api_service

# PROJECT FLASK APP & DATABASE
webApp = ReFlask(__name__)
dtaBse = Database("web.db")


# ======================== WEB APP ROUTE INDEX ========================


# WEB APP DEFAULT HOMEPAGE 
@webApp.end.route('/')
def _home_page_():
    return webApp.html_app("index.html")


# WEB APP API ACCESS PAGE
@webApp.end.route('/api', methods=["GET", "POST"])
def _api_service_():
    return api_service()


# ======================== MAIN.PY _INIT_ FUNC ========================

if __name__ == "__main__":
    
    # IMPORT TABLES
    imported_tables = [
        client_database_tables, 
    ]
    
    # MAKE TABLES THEY DONT EXIST
    for _table in imported_tables:
        for _name, _column in _table:
            dtaBse.new_table(_name, _column)
    dtaBse.db.commit(), dtaBse.db.close()
    
    # -- RUN DEBUG MODE --
    if "debug" in argv:
        basic.__unit_test__()

    # -- RUN WEB APP --
    if "start" in argv:
        webApp.run()
