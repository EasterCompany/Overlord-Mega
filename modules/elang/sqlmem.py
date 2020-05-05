# -*- coding: utf-8 -*-

# STANDARD LIBRARY IMPORTS
from sqlite3 import connect

# PROJECT IMPORTS
from .basic import make_path


""" DATABASE CLASS

  Allows for creating, connecting,
  pushing & pulling from database
  files.
"""


class Database:

    # constructor creates path to local file
    def __init__(self, filename='web.db'):
        self.name = filename.split(".")[0]
        make_path('./.local')
        self.db = connect("./.local/" + self.name + ".db")
        self.sql_cursor = self.db.cursor()

    # queries database, commits & closes
    def sql(self, sql):
        r = self.sql_cursor.execute(sql).fetchall()
        self.commit()
        return r

    # adds data without committing
    def add(self, sql):
        return self.sql_cursor.execute(sql)

    # fetches data without committing
    def get(self, sql, fetch_all=False):
        if fetch_all:
            return self.sql_cursor.execute(sql).fetchall()
        return self.sql_cursor.execute(sql).fetchone()

    # creates a new table; but does not commit or close connection.
    def new_table(self, table_name, columns):
        _columns = ""
        _first_column = None
        for column in columns:
            column = '"' + column[0] + '"	' + column[1]
            if _first_column is None:
                _first_column = ", "
                _columns = _columns + column
            else:
                _columns = _columns + _first_column + column
        return self.add("CREATE TABLE IF NOT EXISTS '" + str(table_name) + "' (" + str(_columns) + ");")

    # commits changes to database and closes the connection
    def commit(self):
        return self.db.commit(), self.db.close()
