# -*- coding: utf-8 -*
# STANDARD LIBRARY IMPORTS
from os import path
from sys import argv, path as sysPath
# E-LANG MODULE IMPORTS
from modules.elang.reflask import ReFlask
# PROJECT DATABASE IMPORTS
from modules.database.client_tables import client_database_tables

# -- APP CONFIGURATION --
overlord = ReFlask(
    "overlord",
    react_enabled=False
)
localDb = "unassigned"
# -----------------------
