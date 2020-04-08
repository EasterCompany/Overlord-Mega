# -*- coding: utf-8 -*-

from os import path, system, chdir, getcwd
from sys import platform, argv
from sqlite3 import connect
from flask import Flask, render_template, redirect, request, jsonify
from modules.elang.basic import make_path, StringWithColour


class ReFlask:

    def __init__(self, _name_):
        # DIRECTORY INITIALIZATION
        make_path("./public")
        make_path("./static/react")
        make_path("./templates")
        # REFLASK INSTANCE OBJECTS
        self.end = Flask(_name_)
        self.rwd = getcwd()
        self.nme = _name_
        # CORE FUNCTIONALITY INITIALIZATION
        if "build" in argv:
            chdir(_name_ + "/")
            system("npm run build")
            chdir(self.rwd)

    def run(self, debug=False):
        self.end.run(debug=debug)

    def html_app(self, route):
        return render_template(route)

    def goto(self, url):
        return redirect(url)

    def form(self, _req=None):
        if _req is None:
            return request.form
        return request.form.get(_req)

    def arg(self, _req=None):
        if _req is None:
            return request.args
        return request.args.get(_req)

    def method(self):
        return request.method

    def redirect(self, href):
        return redirect(href)

    def json(self, to_make):
        return jsonify(to_make)


def webStr(to_format):
    return str(to_format).\
        replace("'", "&apos;").replace(" ", "&nbsp;").\
        replace('"', "	&quot;").replace("<", "&lt;").\
        replace(">", "&gt;")
