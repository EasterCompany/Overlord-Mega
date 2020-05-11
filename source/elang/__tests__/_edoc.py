from source.elang import mock, edoc, deformat
from source.elang.edoc import make, etag

file = mock.file(edoc)
test = file.test

test(
  label="returns a blank e-tag",
  test=edoc.E,
  arg='',
  equals='<!!>',
)

test(
  label="returns an e-tag",
  test=edoc.E,
  arg='etag',
  equals='<!etag!>',
)

test(
  label="returns e-tag in a string",
  test=edoc.etags,
  arg='hello <! world !>',
  equals=['world']
)

test(
  label="returns e-tag(s) in a string",
  test=edoc.etags,
  arg='<!hello!> <! world !>',
  equals=['hello', 'world']
)

txt_test_content = "<html> hello, world! </html>"
txt_test_txt = "&lt;html&gt;&nbsp;hello,&nbsp;world!&nbsp;&lt;/html&gt;"

test(
  label="converts content as txt",
  test=edoc.txt,
  arg=(txt_test_content, False),
  equals=txt_test_txt
)

test(
  label="converts txt as content when reverse parameter is true",
  test=edoc.txt,
  arg=(txt_test_txt, True),
  equals=txt_test_content
)

test_doc = make(name='error', etml='<! test!> ')

test(
  label="can make a default edoc",
  test=make,
  arg='error',
  isNot=None
)

test(
  label="document has correct name",
  test=test_doc.doc['name'],
  equals='error'
)

test(
  label="document build doesn't exist before render",
  test=test_doc.doc,
  notContains='build'
)

test(
  label="document can render",
  test=test_doc.render,
  equals=test_doc.doc
)

test(
  label="document can run",
  test=test_doc.run,
  equals=test_doc.doc['build']
)

test(
  label="document contains a name after render",
  test=test_doc.doc,
  contains='name'
)

test(
  label="document can contain etml",
  test=test_doc.doc,
  contains='etml'
)

test(
  label="document can contain style",
  test=test_doc.doc,
  contains='style'
)

test(
  label="document can contain script",
  test=test_doc.doc,
  contains='script'
)

test(
  label="document contains a raw file path after render",
  test=test_doc.doc,
  contains='file'
)

test(
  label="document contains an app object",
  test=test_doc.doc,
  contains='app'
)

test(
  label="document has a build object to return",
  test=test_doc.doc,
  contains='build'
)

test(
  label="document build result contains style content",
  test=test_doc.doc['build'],
  contains=deformat(etag(test_doc.doc['style'])),
)

test(
  label="document build result contains etml content",
  test=test_doc.doc['build'],
  contains=deformat(etag(test_doc.doc['etml'])),
)

test(
  label="document build result contains script content",
  test=test_doc.doc['build'],
  contains=deformat(etag(test_doc.doc['script'])),
)
