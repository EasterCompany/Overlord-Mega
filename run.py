# ~~~~ DEFINE APP ROUTE INDEX ~~~~
# for app in hosted_apps:
#   webapp.end.register_blueprint(app)
if __name__ == "__main__":
  # import modules
  from src.elang import \
    pyArgs, console, sysPath, path
  
  # interact with console
  sysPath.insert(0, path.dirname(__file__))
  console.clear()
  
  # (optional) run tests
  if "-t" in pyArgs or "test" in pyArgs:
    import test
