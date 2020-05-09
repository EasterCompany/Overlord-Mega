from modules.elang.basic import mock
from modules.elang import reflask

file = mock.file(reflask)
test = file.test

test(
  label="returns a blank e-tag",
  test=reflask.E,
  arg='',
  equals='<!!>',
)

test(
  label="returns an e-tag",
  test=reflask.E,
  arg='etag',
  equals='<!etag!>',
)
