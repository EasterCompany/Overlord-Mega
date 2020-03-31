# -*- coding: utf-8 -*-

# Standard library imports
from os import mkdir, system
from os.path import exists, realpath
from platform import uname
from sys import executable
from urllib.request import urlopen

print(system("python3 -m pip install --upgrade flask"))


# ======================= EASTER LANGUAGE BASIC SUITE ==========================


# Creates a directory path if not exists
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


# Checks if an item is in .gitignore file
def _is_git_ignored(item):
    _found = False
    if exists("./.gitignore"):
        for ignore in open("./.gitignore"):
            if ignore == item:
                _found = True
                break
    return _found 


# Adds an item to .gitignore if not already
def git_ignore(item, display=False):
    if _is_git_ignored(item):
        return True
    if not exists("./.gitignore"):
        open("./.gitignore", "w+")
    
    r = str(open("./.gitignore", "r").read())
    f = open("./.gitignore", "w")
    f.write(r + "\n" + item + "\n")
    f.close()

    if display:
        return print(open("./.gitignore").read())
    elif _is_git_ignored(item):
        return True
    return False

# Fetches information from raw.githubusercontent.com
def git(file_path, repo="documents", branch="master", source="EasterCompany"):
    return urlopen("https://raw.githubusercontent.com/" + \
            source + \
            "/" + repo + \
            "/" + branch + \
            "/" + file_path
        )

# Open, View & Edit a file all at once
def openEdit(path_to_file):
    readOnly = open(path_to_file, "r").read()
    editable = open(path_to_file, "w")
    return readOnly, editable


# Returns input colourful text for console output
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


# Automatically adds a function test to test list
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


# eLang TestSuite Class (wraps test lists & executes tests)
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
            """ + str(self.name) + """
        """ + StringWithColour(self.project).purple() + """
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
                    "\n      ---- " + str(set_name) + \
                        StringWithColour(" completed successfully ").green() + \
                            "----        \n")
            else:
                return print(
            "\n      ---- " + StringWithColour(set_name).pink() + \
            StringWithColour(" had " + str(fails) + " failure(s) ").red() + \
            "----        \n")

    def test(self, name="test name", test_func=[type, "sample test"], expectation=str):

        def passed():
            return " => " + StringWithColour("PASSED").green()

        def failed(tag=name):
            t = StringWithColour(tag).red() + " => " + StringWithColour("FAILED").red()
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
                    return print("      .\n       .\n        .")

        return test()


# ======================== EASTER LANGUAGE TEST SUITE ==========================


# Runs unit tests for this file
def __unit_test__():
    from modules.elang.__test__.basic import make_tests
    te = TestSuite(
        [], 
        _name="elang/basic.py unit test", 
        _post=True, _eject_on_fail=False
        )
    for each in make_tests():
        te.tests = each
        te.run()
