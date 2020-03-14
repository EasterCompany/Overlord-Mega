# -*- coding: utf-8 -*-

# STANDARD LIBRARY IMPORTS
from sys import argv

# EASTER LANGUAGE IMPORTS
from elang import basic
from elang.sqlmem import Database
from elang.reflask import ReFlask

# PROJECT DATABASE IMPORTS 
from modules.database.client_tables import client_database_tables

# PROJECT BACKEND APPLICATIONS
from modules import api_service

# PROJECT GLOBALS
webApp = ReFlask(__name__)
dtaBse = Database(filename="web.db")
_dbtb_ = (client_database_tables, )

# PROJECT MEMORY INITIALIZATION
for _table in _dbtb_:
    for _name, _column in _table:
        dtaBse.new_table(_name, _column)


# ======================== WEB APP ROUTE INDEX ========================


# WEB APP DEFAULT HOMEPAGE 
@webApp.end.route('/')
def _home_page_():
    return webApp.react_app("home-page.html")


# WEB APP BACKEND API INDEX
@webApp.end.route('/api')
def _api_service_():
    return api_service.browser()


# ======================== MAIN.PY _INIT_ FUNC ========================

if __name__ == "__main__":
    if "debug" in argv:
        basic.__unit_test__()
    if "start" in argv:
        if "debug" in argv:
            webApp.run(debug=True)
        else:
            webApp.run()
