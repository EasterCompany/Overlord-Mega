# -*- coding: utf-8 -*-

# STANDARD LIBRARY IMPORTS
from sys import argv
from datetime import datetime
from sqlite3 import connect as db_connect

# EASTER LANGUAGE IMPORTS
from elang import basic
from elang.sqlmem import Database
from elang.reflask import ReFlask, webStr

# PROJECT DATABASE IMPORTS 
from modules.database.client_tables import client_database_tables
from modules.database.helloworld_tables import helloworld_database_tables

# PROJECT BACKEND APPLICATIONS
from modules import api_service

# PROJECT FLASK APP & DATABASE
webApp = ReFlask(__name__)
dtaBse = Database("web.db")
__dt__ = [
    client_database_tables, 
    helloworld_database_tables, 
]

# PROJECT DB TABLES INITIALIZATION
for _table in __dt__:
    for _name, _column in _table:
        dtaBse.new_table(_name, _column)
dtaBse.db.commit(), dtaBse.db.close()

# ======================== WEB APP ROUTE INDEX ========================


# WEB APP DEFAULT HOMEPAGE 
@webApp.end.route('/')
def _home_page_():
    return webApp.html_app("index.html")


# WEB APP API ACCESS PAGE
@webApp.end.route('/api', methods=["GET", "POST"])
def _api_():
    try:
        if webApp.arg("q") == "hello_world":
            if webApp.arg("r") == "posts":
                re = Database().sql(
                    "SELECT * FROM (SELECT * FROM hello_world_posts ORDER BY POST DESC LIMIT 5) ORDER BY POST ASC;"
                )
                se = ""
                for r in re:
                    se = se + "{} {} {}<br>".format(
                        r[0], r[1], r[2])
                return se
            elif webApp.arg("r") == "make_post":
                np = webApp.arg('new_post')
                ps = webApp.arg('new_post_signature')
                Database("web.db").sql(
                    """
                    INSERT INTO hello_world_posts (SIG, CON, TIME) VALUES(
                    '""" + webStr(ps) + """', '""" + webStr(np) + \
                            """', '""" + webStr(datetime.now()) + """'
                        );
                    """
                )
    except Exception as e:
        print(" <API ERROR> ", str(e))
    return webApp.redirect('/')


# ======================== MAIN.PY _INIT_ FUNC ========================

if __name__ == "__main__":
    if "debug" in argv:
        basic.__unit_test__()
    if "start" in argv:
        webApp.run()
