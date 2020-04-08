# IMPORT STANDARD
import os
import sys
import imp
import main

# Initialize main.py like main file
main.__boot__()

# Set working directory
sys.path.insert(0, os.path.dirname(__file__))

# Set working application to eLang backend
application = main.webApp.end
