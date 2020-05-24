from source.elang import mock, comrade as sut

file = mock.file(sut)
test = file.test

# set comrade database as test db
comrade = sut.__comRaid__(raidDB="./.local/dbt")

test(
  label="Check '__test__' doesn't exist in the raid network yet.",
  test=comrade.exists,
  arg="__test__",
  equals=False
)

test(
  label="Add '__test__' to raid network with this system as the owner.",
  test=comrade.share,
  arg=("__test__", 1)
)

test(
  label="Check '__test__' now exists in the raid network.",
  test=comrade.exists,
  arg="__test__",
  equals=True
)

test(
  label="Try upload '__test__' when it already exists in the raid network.",
  test=comrade.share,
  arg=("__test__", 1)
)

test(
  label="Get '__test__' from the raid network (when hosted by self) sometimes doesn't pass on the first test.",
  test=comrade.get,
  arg="__test__",
  equals=('1', 'int')
)

test(
  label="Update '__test__' in the raid network (when hosted by self)",
  test=comrade.raid_update,
  arg=("__test__", 2),
)

test(
  label="Get '__test__' from the raid network (when hosted by self)",
  test=comrade.get,
  arg=("__test__", True),
  equals=2
)

test(
  label="Get '__test__' via api call function",
  test=sut.com_api_request,
  arg=('__test__', comrade),
  equals=("2", "int")
)

def test_api_map_request():
  if sut.host.isSecureServer():
    r = sut.com_api_map_reqest()
    if r is not None:
      return True
  else:
    r = sut.com_api_map_reqest()
    if r is None:
      return True
  return False

test(
  label="Get 'data map' via api call function\n  (should return None on localhost or map data on secure server)",
  test=test_api_map_request,
  equals=True
)

# remove test data and reset tests
comrade.mass.sql("DELETE FROM mass")
comrade.mass.commit()
