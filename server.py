from os import path
from sys import argv, path as sysPath
from overlord import overlord as back

sysPath.insert(0, path.dirname(__file__))
application = back.end

if __name__ == "__main__" and "@ms" in argv:
    if ("test" in argv) or ("debug" in argv):
        from modules.elang.basic import __unit_test__
        __unit_test__()
    elif "test" not in argv:
        application.run()
