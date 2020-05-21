from . import dateTime, undefined, onExit
from .eql import Database
from .basic import formatDateTime
from random import randint


class archive:
  
  def __init__(self, archive_name, default_cols=None):
    self.db = Database(archive_name, path="./.local/dbs")
    self.ar = {
      'id': [],
      'date_added': [],
      'date_modified': [],
    }
    self.max_index = len(self.ar['id'])
    self.nm = archive_name
    self.db.sql("CREATE TABLE IF NOT EXISTS " + archive_name + \
      " ( 'id' INT, 'date_added' datetime, 'date_modified' datetime ) ")
    self.db.db.commit()
    onExit.register(self.db.commit)
    self.rebuild_cols()
    previous_data = self.db.sql("SELECT * FROM " + self.nm)
    self.db.sql("DELETE FROM " + self.nm)
    self.db.db.commit()

    for row in previous_data:
      query_row = []
      for data in row:
        if isinstance(data, str):
          query_row.append("'" + data + "'")
        else:
          query_row.append(str(data))
      
      if row[0] not in self.ar['id']:
        query_row = ", ".join(query_row)
        self.db.add( self.nm, query_row )
        self.db.db.commit()
        for i, a in enumerate(self.ar):
          self.ar[a].append(row[i])
    
    if default_cols is not None:
      for col in default_cols:
        self.add_column(col, default_cols[col])
    
  def index(self):
    self.max_index += 1
    return self.max_index

  def rebuild_cols(self):
    # rebuild columns from table
    cols = self.db.data(self.nm)
    for col in cols:
      self.add_column(col[1], col[2])
    self.db.db.commit()

  def modify(self, data, _id, value):
    self.ar[data][int(_id)] = value
    self.db.sql("UPDATE " + self.nm + " SET " + data + "=" + value + " WHERE id=" + str(_id))
    self.db.db.commit()
    
  def add_column(self, new_col, new_type):
    try:
      if new_col not in self.ar:
        self.ar[new_col] = []
      self.db.sql("ALTER TABLE " + self.nm + " ADD '" +\
        str(new_col) + "' " + str(new_type).upper())
      self.db.db.commit()
    except Exception as add_error:
      if str(add_error).startswith("duplicate column name:"):
        pass
      else:
        print(add_error)

  def make_new_archive(self):
    new_archive = {}
    for data in self.ar:
      if data == 'id':
        new_archive[data] = self.index()
      elif data == 'date_added' or data == 'date_modified':
        new_archive[data] = str(dateTime.now())
      else:
        new_archive[data] = undefined
    return new_archive

  def add(self, archives):
    # Append Archive to RAM Data
    new_archives = []
    for archive in archives:
      new_archives.append(self.make_new_archive())
      new_data_index = 0
      for data in new_archives[-1]:
        if new_archives[-1][data] is undefined:
          new_archives[-1][data] = archive[new_data_index]
          new_data_index += 1
    # Parse Archive for ROM Query
    for archive in new_archives:
      query = ""
      for i, data in enumerate(archive):
        if isinstance(archive[data], str):
          query += "'" + str(archive[data]) + "'"
        else:
          query += str(archive[data])
        if i < len(archive) - 1:
          query += ", "
      if archive['id'] not in self.ar['id']:
        self.db.add(self.nm, query)
  
  def fetch(self, _id):
    d = {}
    for data in self.ar:
      if (_id >= 0 and len(self.ar[data]) > _id) or (_id <= 0 and  0 - len(self.ar) > _id):
        d[data] = self.ar[data][_id]
      else:
        d[data] = "undefined"
    return d
