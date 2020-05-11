from source.elang import mock, server

file = mock.file(server)
test = file.test

test(
  label="server.py can initialize",
  test=server.server.domain,
  equals="easter.company"
)

def isLocalOrSecureOrStable():
  return server.server.isLocalServer() or server.server.isSecureServer() or server.server.isStableServer()

test(
  label="server is localhost, secure or stable",
  test=isLocalOrSecureOrStable,
  equals=True
)

def sslDisabledOnLocal():
  return (server.server.isLocalServer() and not server.server.sslEnabled()) or not server.server.isLocalServer()

test(
  label="server ssl is disabled when locally hosted",
  test=sslDisabledOnLocal,
  equals=True
)

def sslDisabledOnSecure():
  return (server.server.isSecureServer() and not server.server.sslEnabled()) or not server.server.isLocalSecure()

test(
  label="server ssl is disabled when on the secure server",
  test=sslDisabledOnLocal,
  equals=True
)

def sslDisabledOnLocal():
  return (server.server.isStableServer() and server.server.sslEnabled()) or not server.server.isStableServer()

test(
  label="server ssl is enabled when on the stable server",
  test=sslDisabledOnLocal,
  equals=True
)

def serverHasMasterTest():
  return (server.server.isSecureServer() and server.server.server['host'] is None) or \
    (not server.server.isSecureServer() and server.server.server['host'] is not None)

test(
  label="secure server has no master",
  test=serverHasMasterTest,
  equals=True
)

def serverMasterTest():
  return server.server.isSecureServer() or (server.server.server['host'] == "http://secure.easter.company/")

test(
  label="all non-secure servers have secure server has their master",
  test=serverMasterTest,
  equals=True
)
