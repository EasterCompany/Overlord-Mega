# -*- coding: utf-8 -*-

from sys import argv
from elang import basic
from elang.reflask import ReFlask
from PyModules.localDB import localDB

webApp = ReFlask(__name__)


@webApp.end.route('/', methods=['GET', 'POST'])
def home_page():
    return webApp.react_app("home-page.html")


@webApp.end.route('/clients')
def clients_api():
    return webApp.react_app("home-page.html")


if __name__ == "__main__":
    if "debug" in argv:
        basic.__unit_test__()
    if "start" in argv:
        if "debug" in argv:
            webApp.run(debug=True)
        else:
            webApp.run()
