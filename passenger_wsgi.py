# STANDARD LIBRARY IMPORTS ---
import os
import sys
import imp

# WORKING PROJECT IMPORT -----
import main

# SERVER HOST REGISTRATION ---
main.__boot__()
sys.path.insert(0, os.path.dirname(__file__))
application = main.webApp.end
