# IMPORT STANDARD
import os
import sys
import imp

# IMPORT MAIN
import main

# INIT MAIN AS MAIN
main.__boot__()
sys.path.insert(0, os.path.dirname(__file__))

# HOST MAIN AS APP
wsgi = imp.load_source('wsgi', 'main.py')
application = wsgi.webApp.end
