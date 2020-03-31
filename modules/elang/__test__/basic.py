# -*- coding: utf-8 -*-


def make_tests():
    # Easter Language Basic module imports
    from modules.elang.basic import TestSuite, git_ignore
    from modules.elang.basic import exists, make_path, _is_git_ignored
    from modules.elang.basic import StringWithColour
    from modules.elang.basic import _Add_AutoTest_Function

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
        # ELANG basic.py git_ignored Tests
        (
            git_ignore,
                [
                    (git_ignore, "__pycache__/")
                ]
        ),
        # ELANG basic.py _is_git_ignored Tests
        (
            _is_git_ignored,
                [
                    (_is_git_ignored, "__pycache__/")
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
    )
    
    # Easter Language Module - Adds Test Sets to Test Queue
    __sets__ = []
    for Function in Function_tests:
        __sets__.append(_Add_AutoTest_Function(Function[0], Function[1]))
    return __sets__
