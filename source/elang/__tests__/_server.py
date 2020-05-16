from source.elang import mock, server

file = mock.file(server)
test = file.test

test(
  label="server.py can initialize",
  test=server.host.domain,
  equals="easter.company"
)

def isLocalOrSecureOrStable():
  return server.host.isLocalServer() or server.host.isSecureServer() or server.host.isStableServer()

test(
  label="server is localhost, secure or stable",
  test=isLocalOrSecureOrStable,
  equals=True
)

def sslDisabledOnLocal():
  return (server.host.isLocalServer() and not server.host.sslEnabled()) or not server.host.isLocalServer()

test(
  label="server ssl is disabled when locally hosted",
  test=sslDisabledOnLocal,
  equals=True
)

def sslDisabledOnSecure():
  return (server.host.isSecureServer() and not server.host.sslEnabled()) or not server.host.isLocalSecure()

test(
  label="server ssl is disabled when on the secure server",
  test=sslDisabledOnLocal,
  equals=True
)

def sslDisabledOnLocal():
  return (server.host.isStableServer() and server.host.sslEnabled()) or not server.host.isStableServer()

test(
  label="server ssl is enabled when on the stable server",
  test=sslDisabledOnLocal,
  equals=True
)

def serverHasMasterTest():
  return (server.host.isSecureServer() and server.host.server['host'] is None) or \
    (not server.host.isSecureServer() and server.host.server['host'] is not None)

test(
  label="secure server has no master",
  test=serverHasMasterTest,
  equals=True
)

def serverMasterTest():
  return server.host.isSecureServer() or (server.host.server['host'] == "http://secure.easter.company/")

test(
  label="all non-secure servers have secure server has their master",
  test=serverMasterTest,
  equals=True
)
