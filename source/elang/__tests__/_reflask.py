from source.elang import mock, reflask, path

file = mock.file(reflask)
test = file.test

test(
  label="An app can be initialized",
  test=reflask.app,
  arg=('test', False, False),
)

test(
  label="An app can be initialized as a sub-app",
  test=reflask.app,
  arg=('test-sub', False, True),
)

test(
  label="Always contains an error display app",
  test=path.exists,
  arg="./template/app/error/error.html",
  equals=True
)
