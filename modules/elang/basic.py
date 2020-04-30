# -*- coding: utf-8 -*-

# Standard library imports
from os import mkdir, system
from os.path import exists, realpath
from platform import uname
from sys import executable, argv
from urllib.request import urlopen


# ======================= EASTER LANGUAGE BASIC SUITE ==========================


""" install support modules

  installs supported third-party
  modules that may be essential
  to basic functionality. 
  TO DO: ADD OFFLINE SUPPORT
"""


def _install_support_modules(_run_tests=False, *args):
    try:
        if _run_tests:
            from flask import Flask
        else:
            system(realpath(executable) + " -m pip install --upgrade pip")
            system(realpath(executable) + " -m pip install --upgrade flask")
        return True
    except Exception as e:
        return e


if "install" in argv:
    _install_support_modules()


""" DE-FORMAT """


def deformat(string, remove_white_space=False):
    if remove_white_space:
      string = string.replace(" ", "")
    else:
      while "  " in string:
          string = string.replace("  ", " ")
    return string.\
        replace("<! ", "<!").replace(" !>", "!>").\
        replace("\n", "").replace("\r", "").\
        replace("\t", "").replace("\v", "").\
        replace("> <", "><")


""" replace x, and y with r in z """
def listReplace(c, l, r):
    for x in l: 
        c = c.replace(x, r)
    return c


""" MAKE PATH (basic.make_path)

  capable of creating a list
  of directories of embedding
  a new directory within other
  direcotories which may not
  exist.
"""


def make_path(path_to_make, return_path=False):
    p = path_to_make.split('/')
    for i in enumerate(p):
        current_path, j = "", 0
        while j <= i[0]:
            current_path, j = current_path + p[j] + '/', j + 1
        if not exists(current_path):
            mkdir(current_path)
    if return_path:
        return path_to_make
    return exists(path_to_make)


""" git (basic.git)

  returns contents of a
  raw.githubusercontent
  repo file
"""


def git(file_path, repo="Overlord", branch="master", source="EasterCompany"):
    try:
        return urlopen("https://raw.githubusercontent.com/" +
                       source + "/" + repo + "/" + branch + "/" + file_path).read().decode('utf-8')
    except Exception as error:
        return error


""" String With Colour (basic.StringWithColour)

  returns a string surrounded by
  BASH / BATCH colour code tags
"""


class StringWithColour:
    content = None
    endOfString = '\033[0m'

    def __init__(self, as_string_with_colour=""):
        self.content = str(as_string_with_colour)

    def _string_(self, string=""):
        if self.content is not None:
            return str(self.content)
        return string

    def white(self, string=""):
        return '\033[97m' + self._string_(string) + self.endOfString

    def blue(self, string=""):
        return '\033[96m' + self._string_(string) + self.endOfString

    def pink(self, string=""):
        return '\033[95m' + self._string_(string) + self.endOfString

    def purple(self, string=""):
        return '\033[94m' + self._string_(string) + self.endOfString

    def yellow(self, string=""):
        return '\033[93m' + self._string_(string) + self.endOfString

    def green(self, string=""):
        return '\033[92m' + self._string_(string) + self.endOfString

    def red(self, string=""):
        return '\033[91m' + self._string_(string) + self.endOfString


# ======================== EASTER LANGUAGE TEST SUITE ==========================

""" Add Auto-test Function (basic._Add_AutoTest_Function)

  Creates a new automatic test for a
  function or functions of a class
  and adds the test to a list of tests
"""


def _Add_AutoTest_Function(_class, _funcs):
    __tests__ = []
    for f in _funcs:
        __tests__.append(
            (
                str(_class),
                (
                    f[0],
                    f[1]
                ), True
            )
        )
    return __tests__


""" ELANG TEST SUITE (basic.TestSuite)

  Wraps a test list and executes tests
  with a report on success and failure
  should also report failures on live
  platforms.
"""


class TestSuite:

    def __init__(self, tests, _name="__TestSuite__", _post=False, _eject_on_fail=True):
        self.post = _post
        self.eject_on_fail = _eject_on_fail
        self.name = _name
        self.tests = tests
        self.fails = 0
        self.test_index = 0
        self.project = realpath(".").split('/')[-1]
        if self.post:
            print("""
  """ + str(self.name) + ": " + StringWithColour(self.project).purple() + """
  DIST: """ + uname()[0] + """
  NAME: """ + uname()[1] + """
  PROJECT DIR: """ + realpath(".").split('/' + self.project)[0] + """
  PYTHON  INT: """ + realpath(executable))

    def run(self):
        name = None
        for self.test_index, test in enumerate(self.tests):
            name = test[0]
            self.test(name=test[0], test_func=test[1], expectation=test[2])
        return self.finish(name)

    def finish(self, set_name):
        fails, self.fails = self.fails, 0
        if self.post:
            if fails == 0:
                return print(
                    "\n 		 ---- " + StringWithColour(set_name).purple() +
                    StringWithColour(" completed successfully ").green() +
                    "---- 			 \n")
            else:
                return print(
                    "\n 		 ---- " + StringWithColour(set_name).pink() +
                    StringWithColour(" has " + str(fails) + " failure(s) ").red() +
                    "---- 			 \n")

    def test(self, name="test name", test_func=[type, "sample test"], expectation=str):

        def passed():
            return " => " + StringWithColour("PASSED").green()

        def failed(tag=name):
            t = StringWithColour(tag).red() + " => " + \
                StringWithColour("FAILED").red()
            if self.eject_on_fail:
                t = t + "\n"
            else:
                self.fails = self.fails + 1
            return t

        def unit(fin, tar=test_func, res=expectation):
            return """
  UNIT TEST """ + name + """
  { """ + str(tar) + """ }
  { """ + str(res) + """ } """ + str(fin)

        def test(t=test_func[0](test_func[1]), r=expectation):
            if (t == r) or (callable(r) and r()):
                _test_ = "passed"
            else:
                _test_ = "failed"
            if _test_ == "failed" and self.eject_on_fail:
                _test_ = failed()
                _unit_ = unit(_test_)
                return print(_unit_), exit()
            elif self.post:
                if _test_ == "passed":
                    _test_ = passed()
                else:
                    _test_ = failed()

                if len(self.tests) <= 4 or \
                    self.test_index == len(self.tests) - 1 or \
                        self.test_index == 0:
                    return print(unit(_test_))
                elif self.test_index == len(self.tests) - 2:
                    return print(StringWithColour("\n  .\n  . .\n  . . .").purple())

        return test()


# ======================== EASTER LANGUAGE TEST SUITE ==========================


""" Unit Test (elang.__unit_test__)
  Runs elang's unit tests
"""


def __unit_test__():
    from modules.elang.__test__.overlord import make_tests
    te = TestSuite(
        [],
        _name="ELANG",
        _post=True, _eject_on_fail=True
    )
    for each in make_tests():
        te.tests = each
        te.run()
