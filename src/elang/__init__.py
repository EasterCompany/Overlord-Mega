# Standard Library Extensions
import atexit as onExit
from os import \
  mkdir as mkDir, chdir as chDir, \
  getcwd as workDir, walk as walkDir, \
  system as console, path, name as sysOS
from sys import \
  executable as pyExe, argv as pyArgs, path as sysPath
from urllib.request import \
  urlopen as openUrl
from sqlite3 import \
  connect as loadDatabase
from datetime import \
  datetime
from time import \
  time as sysTime, sleep as sysSleep

# Python Language Extenders
from .basic import \
  undefined, crashed

# Python Console Extensions
from .basic import \
  strColor, sysName, console, mock
