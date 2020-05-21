from source.elang import archive as sut
from source.elang import mock

file = mock.file(sut)
test = file.test

test_archive = sut.archive('test')

test(
    label="add integer column to archive",
    test=test_archive.add_column,
    arg=('test_int', 'int')
)

test(
    label="add text column to archive",
    test=test_archive.add_column,
    arg=('test_txt', 'text')
)

test(
    label="add input to archive",
    test=test_archive.add(
        [
            (1, 'one'), 
            (2, 'two')
        ]
    ),
)

test(
    label="can fetch archived data(id) from id number",
    test=test_archive.fetch(0)['id'],
    equals=1
)

test(
    label="can fetch archived data(value) from id number",
    test=test_archive.fetch(0)['test_txt'],
    equals='one'
)

test(
    label="no duplicate records were made",
    test=len,
    arg=test_archive.db.sql("SELECT * FROM " + test_archive.nm + " WHERE id=1 LIMIT 2;"),
    equals=1
)

# tests will fail if database is not committed
test_archive.db.commit()
