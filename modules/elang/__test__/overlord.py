# -*- coding: utf-8 -*-
from modules.elang.basic import *
from modules.elang.basic import _install_support_modules
from modules.elang.basic import _Add_AutoTest_Function
from modules.elang.reflask import *

""" MAKE TESTS (test)

  imports required modules from eLang.basic
  and tests functionality for expected output
"""


def make_tests():
    # BASIC tests
    def test_deformat(text): return deformat(text).replace(" ", "") == ""
    def test_deformat_html(text): return deformat(text) == "><"
    def test_deformat_etag(text): return deformat(text) == "<!!>"

    def test_git(_file):
        _git = git(_file)
        _raw = open("./README.md").read()
        if _git == _raw:
            return True
        else:
            if "[Errno -2]" in str(_git):  # INTERNET CONNECTION EXCEPTION
                print(
                    """
    basic.git passed with exception -:
    """, StringWithColour(_git).blue())
                return True
            elif not isinstance(_git, str):  # README WAS MODIFIED EXCEPTION
                return False
            else:
                return True

    # REFLASK tests
    def test_reflask_initializes(sut): return ("overlord" == sut().nme)

    Function_tests = (
        (
            "basic.py",
            [
                (make_path, "__pycache__/__tests__/__cache__"),
                (exists, "__pycache__/__tests__/__cache__"),
                (test_deformat, "  \n  \t  \r  \v  "),
                (test_deformat_etag, "<! !>"),
                (test_deformat_html, "> <"),
                (_install_support_modules, True),
                (test_git, "README.md"),
                (StringWithColour(
                    "wht").white().startswith, '\033[97m'),
                (StringWithColour(
                    "-:-").white().endswith, "\x1b[0m"),
            ]
        ),
        (
            "reflask.py",
            [
                (test_reflask_initializes, ReFlask)
            ]
        ),
    )

    # Adds Test Sets to Test Queue
    __sets__ = []
    for Function in Function_tests:
        __sets__.append(_Add_AutoTest_Function(Function[0], Function[1]))
    return __sets__
