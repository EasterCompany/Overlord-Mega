# -*- coding: utf-8 -*-

# FLASK ROOT ELEMENT
from flask import Flask, request, redirect
application = Flask(__name__)


# eLANG FRONTEND CONTROL CENTRE
@application.route('/eLang/frontend', method=['GET', 'POST'])
def eLang_frontend_control_centre():
    if request.args.get('q') is not None:
        return str(request.args.get('q'))
    return ""


# eLANG BACKEND OPERATIONS CENTRE
@application.route('/eLang/backend', method=['GET', 'POST'])
def eLang_backend_operations():
    if request.args.get('q') is not None:
        return str(request.args.get('q'))
    return ""

