# -*- coding: utf-8 -*-


""" MAKE TESTS (test)

    imports required modules from eLang.basic
    and tests functionality for expected output
"""


def make_tests():
    # BASIC
    from modules.elang.basic import TestSuite, exists, make_path
    from modules.elang.basic import StringWithColour
    from modules.elang.basic import _Add_AutoTest_Function
    from modules.elang.basic import _install_support_modules
    # REFLASK
    from modules.elang.reflask import ReFlask

    def _test_reflask_initializes(sut): return ("test" == sut().nme)

    # eLang/basic.py Module Function Tests
    Function_tests = (

        # ELANG basic.py make_path Tests
        (
            make_path,
            [
                (make_path, "__pycache__/__tests__/__cache__")
            ]
        ),
        # ELANG basic.py exists Tests
        (
            exists,
            [
                (exists, "__pycache__/__tests__/__cache__")
            ]
        ),
        # ELANG basic.py StringWithColour Tests
        (
            StringWithColour,
            [
                # CHECK: string color code opens
                (StringWithColour("red").red().startswith, '\033[91m'),
                (StringWithColour("grn").green().startswith, '\033[92m'),
                (StringWithColour("ylw").yellow().startswith, '\033[93m'),
                (StringWithColour("prp").purple().startswith, '\033[94m'),
                (StringWithColour("pnk").pink().startswith, '\033[95m'),
                (StringWithColour("blu").blue().startswith, '\033[96m'),
                (StringWithColour("wht").white().startswith, '\033[97m'),
                # CHECK: string color code closes
                (StringWithColour("-:-").red().endswith, "\x1b[0m"),
                (StringWithColour("-:-").green().endswith, "\x1b[0m"),
                (StringWithColour("-:-").yellow().endswith, "\x1b[0m"),
                (StringWithColour("-:-").purple().endswith, "\x1b[0m"),
                (StringWithColour("-:-").pink().endswith, "\x1b[0m"),
                (StringWithColour("-:-").blue().endswith, "\x1b[0m"),
                (StringWithColour("-:-").white().endswith, "\x1b[0m"),
            ]
        ),
        (
            _install_support_modules,
            [
                (_install_support_modules, True)
            ]
        ),
        (
            _test_reflask_initializes,
            [
                (_test_reflask_initializes, ReFlask)
            ]
        )
    )

    # Easter Language Module - Adds Test Sets to Test Queue
    __sets__ = []
    for Function in Function_tests:
        __sets__.append(_Add_AutoTest_Function(Function[0], Function[1]))
    return __sets__
