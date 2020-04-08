# IMPORT STANDARD
import os
import sys
import imp
import main

main.__boot__()  # Initialize main.py like main file
sys.path.insert(0, os.path.dirname(__file__))  # Set working directory
application = main.webApp.end  # Set working application to eLang backend
