
# STANDARD LIBRARY IMPORTS
from . import loadDB, mkDir


class Database:

    # constructor creates path to local file
    def __init__(self, filename='main', path='./.local/dbs'):
        self.name = filename
        mkDir(path)
        self.db = loadDB(path + "/" + self.name + ".mem")
        self.sql_cursor = self.db.cursor()

    # queries database for columns within a table
    def data(self, table):
        return self.sql("PRAGMA table_info(" + table + ");")

    # queries database, commits & closes
    def sql(self, sql):
        r = self.sql_cursor.execute(sql).fetchall()
        return r

    # adds data without committing
    def add(self, to_table, values):
        return self.sql_cursor.execute("INSERT INTO " + to_table + " VALUES(" + values + ");")

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
        return self.sql("CREATE TABLE IF NOT EXISTS '" + str(table_name) + "' (" + str(_columns) + ");")

    # commits changes to database and closes the connection
    def commit(self):
        try:
            return self.db.commit(), self.db.close()
        except Exception as e:
            print('[ DATABASE ERROR: ' + str(e) + ' ]')

    # import a schema into this database
    def import_schema(self, schema):
        for table in schema.tables:
            values = []
            for column in schema.tables[table]:
                values.append(column + " " + schema.tables[table][column])
            if len(values) > 0:
                query = \
                "CREATE TABLE IF NOT EXISTS " + table + " (" + ', '.join(values) + ");"
                self.sql(query)
