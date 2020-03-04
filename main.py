#! /usr/bin/env python3 
# -*- coding: utf-8 -*-

# IMPORT STANDARD LIBRARY
import os
import sys
import socket
import subprocess
from flask import Flask

# FLASK APP
app = Flask(__name__)

# FLASK PAGE INDEX MANAGER
from flaskApps.index import *

# ON-BOOT INITIALIZATION
if __name__ == "__main__":
    if 'debug' in str(sys.argv):
        app.run(debug=True)
