from modules.elang.basic import mock, path
from modules.elang import sqlmem
from modules.elang.sqlmem import Database

# MOCK VARIABLES -----------
file = mock.file(sqlmem)
test = file.test

testDB = Database('test', './test/.local/dbs')
newDB = Database("test", './test/.local/dbs')
delDB = Database("test", './test/.local/dbs')

# MOCK FUNCTIONS -----------
def test_closed_database():
  d = Database('test', './test/.local/dbs')
  d.commit()
  try:
    d.get("SELECT * FROM test")
  except Exception as e:
    return str(e)
  return False

def test_database_closes():
  r = False
  try:
    newDB.get("SELECT * FROM test")
  except Exception as e:
    if not r:
      r = "couldn't close delDB"
    else:
      r = True
  try:
    delDB.get("SELECT * FROM test")
  except Exception as e:
    if not r:
      r = "couldn't close newDB"
    else:
      r = True
  return r

def test_data_with_commit():
  r = newDB.get("SELECT * FROM test LIMIT 1;")
  newDB.commit()
  return r

def test_data_after_delete():
  r = delDB.sql("DELETE FROM test WHERE test=1")
  delDB.commit()
  return len(r)


def test_add_data():
  testDB.add("test", "'1', 'test'")
  return testDB.get("SELECT * FROM test LIMIT 1;")


def test_without_commit():
  return testDB.commit()

# MODULE UNIT TESTS 
test(
  label="try create a test database",
  test=Database,
  arg=('test', './test/.local/dbs'),
  isNot=None
)

test(
  label="check the test database has been created",
  test=path.exists,
  arg="./test/.local/dbs/test.db",
  equals=True
)

test(
  label="try close the test database",
  test=test_closed_database,
  equals="Cannot operate on a closed database."
)

test(
  label="try make a new table in the test database",
  test=testDB.new_table,
  arg=(
    'test',
    [
      ('test', 'INT'),
      ('_test', 'TEXT')
    ]
  ),
  equals=[],
)

test(
  label="try select items from the new table.",
  test=testDB.get,
  arg="SELECT * FROM test LIMIT 1;",
  equals=None
)

test(
  label="try add items to the new table.",
  test=test_add_data,
  equals=(1, 'test')
)

test(
  label="try retreiving information from a database that was not saved.",
  test=test_without_commit,
  equals=(None, None)
)

test(
  label="try retrieve information from a database that was saved successfully.",
  test=test_data_with_commit,
  equals=(1, 'test')
)

test(
  label="try retrieve information from a database after it has been deleted.",
  test=test_data_after_delete,
  equals=0
)

test(
  label="try retrieve information from a database when the connection has been closed.",
  test=test_database_closes,
  equals=True
)
