# -*- coding: utf-8 -*-

# STANDARD LIBRARY IMPORTS
from sqlite3 import connect

# E-LANG MODULE IMPORTS
from modules.elang.basic import make_path


""" DATABASE CLASS

    Allows for creating, connecting,
    pushing & pulling from database
    files.                       
"""
class Database:

    def __init__(self, filename='web.db'):
        make_path('./.local')
        self.db = connect("./.local/" + filename)
        self.sql_cursor = self.db.cursor()
        self.name = filename

    def sql(self, sql):
        r = self.sql_cursor.execute(sql).fetchall()
        self.db.commit(), self.db.close()
        return r

    def add(self, sql):
        return self.sql_cursor.execute(sql)

    def get(self, sql, fetch_all=False):
        if fetch_all:
            return self.sql_cursor.execute(sql).fetchall()
        return self.sql_cursor.execute(sql).fetchone()

    def new_table(self, name, columns):
        _columns = ""
        _first_column = None
        for column in columns:
            column = '"' + column[0] + '"	' + column[1]
            if _first_column is None:
                _first_column = ", "
                _columns = _columns + column
            else:
                _columns = _columns + _first_column + column
        return self.add("CREATE TABLE IF NOT EXISTS '" + str(name) + "' (" + str(_columns) + ");")
