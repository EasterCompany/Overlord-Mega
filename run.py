# ~~~~ DEFINE APP ROUTE INDEX ~~~~
# for app in hosted_apps:
#   webapp.end.register_blueprint(app)
if __name__ == "__main__":
  
  # import modules
  from source.elang import \
    pyArgs, console, sysPath, path
  
  # interact with console
  sysPath.insert(0, path.dirname(__file__))
  console.clear()
  
  # (optional) install dependencies
  if "-i" in pyArgs or "install" in pyArgs:
    from source.elang.basic import __install__
    __install__()

  # (optional) update source
  if "-u" in pyArgs or "update" in pyArgs:
    from source.elang.basic import __gitUpdate__
    __gitUpdate__()

  # (optional) run tests
  if "-t" in pyArgs or "test" in pyArgs:
    console.clear()
    from source.elang import __tests__
