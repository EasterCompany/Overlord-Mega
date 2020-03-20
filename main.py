# -*- coding: utf-8 -*-

# STANDARD LIBRARY IMPORTS
from sys import argv
from sqlite3 import connect as db_connect

# EASTER LANGUAGE IMPORTS
from elang import basic
from elang.sqlmem import Database
from elang.reflask import ReFlask

# PROJECT DATABASE IMPORTS 
from modules.database.client_tables import client_database_tables
from modules.database.helloworld_tables import helloworld_database_tables

# PROJECT BACKEND APPLICATIONS
from modules import api_service

# PROJECT GLOBALS
webApp = ReFlask(__name__)
dtaBse = Database("web.db")
_dbtb_ = [
    client_database_tables, 
    helloworld_database_tables, 
]

# PROJECT MEMORY INITIALIZATION
for _table in _dbtb_:
    for _name, _column in _table:
        dtaBse.new_table(_name, _column)
dtaBse.db.commit(), dtaBse.db.close()


# ======================== WEB APP ROUTE INDEX ========================


# WEB APP DEFAULT HOMEPAGE 
@webApp.end.route('/')
def _home_page_():
    return webApp.html_app("index.html")


# HELLO WORLD POST-TO PAGE
@webApp.end.route('/make/post')
def _make_post_():
    np = webApp.arg('new_post')
    ps = webApp.arg('new_post_signature')
    Database("web.db").sql(
        """
        INSERT INTO hello_world_posts VALUES(
           '""" + ps + """', '""" + np + """'
            );
        """
    )
    return webApp.redirect('/')


# WEB APP API ACCESS PAGE
@webApp.end.route('/api', methods=["GET", "POST"])
def _api_():
    if webApp.arg("q") == "hello_world":
        if webApp.arg("r") == "posts":
            re = Database("web.db").sql(
                "SELECT * FROM hello_world_posts LIMIT 10;")
            se = str()
            for r in re:
                se = se + "{" + " '{}': '{}', '{}': '{}', ".format("n", r[0], "c", r[1]) + "}"
            return webApp.json(to_make=se)
    return ""


# ======================== MAIN.PY _INIT_ FUNC ========================

if __name__ == "__main__":
    if "debug" in argv:
        basic.__unit_test__()
    if "start" in argv:
        webApp.run()
