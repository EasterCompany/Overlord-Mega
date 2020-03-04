#! /usr/bin/env python3 
# -*- coding: utf-8 -*-

"""
passenger_wsgi.py file is reserved for server deployment
    do not remove - do not edit - do not disturb
"""

import os
import sys
from main import app as application
sys.path.insert(0, os.path.dirname(__file__))
