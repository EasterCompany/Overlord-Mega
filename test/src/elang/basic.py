# TEST MODULE -----------------
from src.elang.basic import mock

# MODULE TO TEST --------------
from src.elang import basic

# MOCK VARIABLES --------------
file = mock.file(basic)
test = file.test

# MODULE UNIT TESTS -----------
test(
  label="test python pip modules CAN and HAVE been installed.",
  test=basic.__install__,
  arg=True,
  equals=True
)

test(
  label="test git repo can be commanded to update.",
  test=basic.__gitUpdate__,
  arg=True,
  equals=True
)

test(
  label="can deformat tabs to double spaces.",
  test=basic.deformat,
  arg="hello\tworld!",
  equals="hello  world!"
)

test(
  label="can deformat tabs to nothing and remove new lines",
  test=basic.deformat,
  arg=("hello-\n\tworld!", True),
  equals="hello-world!"
)

test(
  label="can deformat all formating but keep spacing (and tabs as double spaces).",
  test=basic.deformat,
  arg="hello, \n\r\t world!",
  equals="hello,  world!"
)

test(
  label="return content; with list contents replaced with variable 'r'",
  test=basic.listReplace,
  arg=("abc123xyz", ['1', '2', '3'], '.'),
  equals="abc...xyz",
)

test(
  label="can created a directory nested in multiple non-existent directories",
  test=basic.make_path,
  arg=('./test/.local/dbs', True),
  equals=True
)

test(
  label="retrieves raw content from github repo file (*requires readme to be up-to-date in commit*)",
  test=basic.git,
  arg="README.md",
  equals=open("./README.md").read()
)
