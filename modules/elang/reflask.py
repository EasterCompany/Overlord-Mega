# -*- coding: utf-8 -*-

from os import path, system, chdir, getcwd
from sys import platform, argv
from sqlite3 import connect
from flask import Flask, render_template, redirect, request, jsonify
from modules.elang.basic import make_path, StringWithColour


class ReFlask:

    def __init__(self, _name_):
        # DIRECTORY INITIALIZATION
        make_path("./public")               # PUBLIC INFORMATION
        make_path("./static/react")         # GYPSY LOCAL CACHE
        make_path("./templates/objects")    # HTML/CSS/JS Objects
        make_path("./templates/pages")      # HTML/CSS/JS Templates
        # REFLASK INSTANCE OBJECTS
        self.end = Flask(_name_)            # Backend app
        self.rwd = getcwd()                 # Server Working Directory
        self.nme = _name_                   # Frontend app
        # CORE FUNCTIONALITY INITIALIZATION
        if "build" in argv:
            chdir(_name_ + "/")
            system("npm run build")
            chdir(self.rwd)

    def run(self, debug=False):
        self.end.run(debug=debug)

    def html_app(self, route):
        # Open HTML_ROOT file
        OUTPUT = open("templates/pages/" + route).read()
        # Set HTML Parser Settings
        include_css = False
        include_obj = False
        # Remove redundent spacing
        while "  " in OUTPUT:
            OUTPUT = OUTPUT.replace("  ", " ")
        # Split OUTPUT for eTags
        OUTPUT = OUTPUT.\
            replace("<! ", "<!").\
            replace(" !>", "!>").split("<! ")
        # If any eTags in ROOT file
        if isinstance(OUTPUT, list):
            for i, tag in enumerate(OUTPUT):
                # Find tag content and remove white space
                tag = tag.split("!>")[0].replace(" ", "")
                # Define eTag HTML inclusions
                if tag.startswith("include:"):
                    if tag.endswith("css"):
                        # when including css
                        include_css = True
                        css_inclusions = []
                    elif tag.endswith("obj"):
                        # when including objs
                        include_obj = True
                # Inclusions
                if include_css:
                    return css_inclusions
                if include_obj:
                    return include_obj
        return OUTPUT

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
