from . import dataType
from .eql import Database
from .schema import comRaid
from .server import host
from .reflask import main


class __comRaid__:

  def __init__(self, raidDB="./.local/dbs"):
    self.mass = Database('comRaid', raidDB)
    self.mass.import_schema(comRaid)
    self.map = {}
    self.name = host.url()

  def exists(self, name):
    return name in self.map
  
  def owns(self, name):
    return self.exists(name) and self.map[name] == self.name

  def save(self):
    self.mass.db.commit()

  def close(self):
    self.mass.db.close()

  def get(self, name, raw=False):
    if self.owns(name):
      r = self.mass_fetch(name)
    else:
      return None
    if raw and r is not None:
      if r[1] == 'list': return r[0].split(' ')
      elif r[1] == 'int': return int(r[0])
    return r

  def share(self, name, value):
    if not self.owns(name):
      if not self.exists(name):
        self.map[name] = self.name
        self.add_to_local_mass(name, value)
        self.save()

  def add_to_local_mass(self, name, value):
    if self.owns(name):
      values = "'" + str(name) + "', '" + str(value) + \
              "', '" + dataType(value) + "'"
      self.mass.add("mass", values)

  def mass_fetch(self, name):
    return self.mass.get("SELECT value, type FROM mass WHERE name='" + name + "' LIMIT 1;")

  def mass_update(self, name, value):
    if self.owns(name):
      self.mass.sql("DELETE FROM mass WHERE name='" + name + "'")
      self.save()
      self.add_to_local_mass(name, value)
      self.save()


comrade = __comRaid__()


def api_request(name, unit=comrade):
  if unit.owns(name):
    return unit.get(name)
  return None

