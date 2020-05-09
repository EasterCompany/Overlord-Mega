from src.elang.edoc import eDoc

home = eDoc('home')


@home_app.route('/')
def index():
  return home.run()
