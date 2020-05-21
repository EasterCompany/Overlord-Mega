

def run():
  from source.elang import pyArgs
  from __app__ import webApp
  n = False
  for arg in pyArgs:
    if arg == "-m" or arg == "make-web-app":
      n = True
    elif n:
      webApp.has_app(arg)
      break

