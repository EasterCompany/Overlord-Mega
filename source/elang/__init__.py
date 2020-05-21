# Python 2 / 3 Test
try:
  from urllib.request import urlopen as openUrl
except Exception as e:
  if 'No module named request' in str(e):
    print("Python 2 is not compatible with Overlord. (use python 3.2 or greater)")
    exit()

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
  crypt, \
  strColor, \
  sysName, \
  console, \
  mock, \
  deformat, \
  dataType, \
  listReplace, \
  __install__, \
  __gitUpdate__

# Optional inits
from source.elang.__tests__ import run_elang_tests
from source.scripts import host_server
from source.scripts import make_web_app
inits = []
optional_inits = {
  'install': __install__,
  'update': __gitUpdate__,
  'test': run_elang_tests,
  'server': host_server.run,
  'make-app': make_web_app.run
}

# (if any) Parse & init user input parameters
for init in optional_inits:
  if init in pyArgs or "-" + init[0] in pyArgs:
    optional_inits[init]()
