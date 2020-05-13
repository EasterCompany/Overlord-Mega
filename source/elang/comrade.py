from .eql import Database


class comRaid:

  def __init__(self):
    self.db = Database('comraid', './.local/dbs')
