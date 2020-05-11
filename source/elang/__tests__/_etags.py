from source.elang import mock, etags

file = mock.file(etags)
test = file.test

test(
  label="<! test !>",
  test=etags.eTags['test'],
  equals='<!-- pass -->'
)
