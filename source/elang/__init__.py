# Standard Library Extensions
import atexit as onExit
from os import \
  chdir as chDir, \
  getcwd as workDir, \
  walk as walkDir, \
  path, \
  name as sysOS
from sys import \
  executable as pyExe, \
  argv as pyArgs, \
  path as sysPath
from urllib.request import \
  urlopen as openUrl
from sqlite3 import \
  connect as loadDB
from datetime import \
  datetime as dateTime
from time import \
  time as sysTime, \
  sleep as sysSleep

# Python Language Extenders
from .basic import \
  undefined, \
    crashed

# Python Console Extensions
from .basic import \
  make_path as mkDir, \
  strColor, \
  sysName, \
  console, \
  mock, \
  deformat, \
  listReplace
