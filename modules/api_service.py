# -*- coding: utf-8 -*-

from flask import request, jsonify


def browser():
    return jsonify(request.args)