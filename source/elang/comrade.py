from . import dataType, onExit
from .eql import Database
from .schema import comRaid
from .server import host, api


class __comRaid__:

  def __init__(self, raidDB="./.local/dbs"):
    self.data = ('cR', raidDB)
    self.mass = Database(self.data[0], self.data[1])
    self.mass.import_schema(comRaid)
    self.map = {}
    self.reqHistory = []
    for data in self.mass.get("SELECT * FROM mass", fetch_all=True):
      self.map[data[0]] = (data[1], data[2])
    self.name = host.url()
    self.save()

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
      return api("cGet", (host.server['name'], name))
    if raw and r is not None:
      if r[1] == 'list': return r[0].split(' ')
      elif r[1] == 'int': return int(r[0])
    return r

  def share(self, name, value, _type=None):
    if not self.owns(name) and not self.exists(name):
      self.map[name] = self.name
      self.add_to_local_mass(name, value, _type)
      if host.server['host'] is not None:
        try:
          api(
            service="cShare", 
            args=(host.server['name'], name, 'link')
          )
          for req in self.reqHistory:
            api(req[1], req[2])
          self.reqHistory = []
        except Exception as error:
          if 'Errno -2' in str(error):
            self.reqHistory.append(('cShare', (host.server['name'], name, 'link')))

  def add_to_local_mass(self, name, value, _type=None):
    self.mass = Database(self.data[0], self.data[1])
    if self.owns(name):
      if _type is None: _type = dataType(value)
      values = "'" + str(name) + \
        "', '" + str(value) + \
        "', '" + _type + "'"
      self.mass.add("mass", values)
      self.save()

  def mass_fetch(self, name):
    return self.mass.get("SELECT value, type FROM mass WHERE name='" + name + "' LIMIT 1;")

  def mass_update(self, name, value, _type=None):
    if self.owns(name):
      if _type is None: 
        _type = dataType(value)
      self.mass.sql("DELETE FROM mass WHERE name='" + name + "'")
      self.save()
      self.add_to_local_mass(name, value, _type)
      self.save()


comrade = __comRaid__()


def com_api_request(req, unit=comrade):
  if unit.owns(req):
    return unit.get(req)
  return None


def com_api_map_reqest(unit=comrade):
  if host.hasNoMaster():
    return unit.map


@onExit.register
def onExitFunction():
  comrade.close()
