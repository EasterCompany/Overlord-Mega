from . import \
  mkDir, path, datetime, \
  pyArgs, pyExe, openUrl, \
  sysTime, sysSleep, sysOS
from platform import uname
from os import system as _console


# PyLanguage Extensions
def __undefined__():
  pass
def __crashed__():
  pass


# Python Language Extenders
undefined = __undefined__
crashed = __crashed__
sysName = uname().node

# PyArgument Extension
def __defined__(arg):
  return arg != undefined


# Python Argument Extension
defined = __defined__


# Python Pip Module Installation
def __install__(__testfunction__=False):
  if __testfunction__:
    try:
      from flask import Flask
    except:
      return False
    return True
  else:
    console(path.realpath(pyExe) + " -m pip install --upgrade pip")
    console(path.realpath(pyExe) + " -m pip install --upgrade flask")


# Git Pull Command Function
def __gitUpdate__(__testfunction__=False):
  if __testfunction__:
    return path.exists('./.git')
  console("git pull")


# Makes A String More Machine Readable
def deformat(string, remove_white_space=False, *args):
  string = string.\
    replace("<! ", "<!").replace(" !>", "!>").\
    replace("\n", "").replace("\r", "").\
    replace("\v", "")
  if remove_white_space:
    string = string.replace(" ", "").replace("\t", "")
  else:
    while "  " in string:
      string.replace("  ", " ")
    string = string.replace(" \t", "\t")
    string = string.replace("\t ", "\t")
    string = string.replace("\t", "  ")
  return string


# return content; with list contents replaced with variable 'r'
def listReplace(c, l, r):
  for x in l: 
    c = c.replace(x, r)
  return c


# Makes Multiple Directories From Path String
def make_path(path_to_make, __testfunction__=False):
  p = path_to_make.split('/')
  for i in enumerate(p):
    current_path, j = "", 0
    while j <= i[0]:
      current_path, j = current_path + p[j] + '/', j + 1
    if not path.exists(current_path):
      mkDir(current_path)
  if __testfunction__:
    return path.exists(path_to_make)
  return path_to_make


# return content raw.githubusercontent file content
def git(file_path, repo="Overlord", branch="master", source="EasterCompany"):
  try:
    return openUrl("https://raw.githubusercontent.com/" +
             source + "/" + repo + "/" + branch + "/" + file_path).read().decode('utf-8')
  except Exception as error:
    return error


# ENCLOSE A STRING WITH COLOUR TAGS
class __strColor__:
  content = None
  close_string = '\033[0m'

  def __init__(self, as_string_with_colour=""):
    self.content = str(as_string_with_colour)

  def white(self, string=""):
    return '\033[97m' + str(string) + self.close_string

  def cyan(self, string=""):
    return '\033[96m' + str(string) + self.close_string

  def purple(self, string=""):
    return '\033[95m' + str(string) + self.close_string

  def blue(self, string=""):
    return '\033[94m' + str(string) + self.close_string

  def yellow(self, string=""):
    return '\033[93m' + str(string) + self.close_string

  def green(self, string=""):
    return '\033[92m' + str(string) + self.close_string

  def red(self, string=""):
    return '\033[91m' + str(string) + self.close_string
  
  def black(self, string=""):
    return '\033[90m' + str(string) + self.close_string
  
  def scored(self, string=""):
    return '\033[9m' + str(string) + self.close_string   
  
  def invisible(self, string=""):
    return '\033[8m' + str(string) + self.close_string  
  
  def highlight(self, string=""):
    return '\033[7m' + str(string) + self.close_string
    
  def blink(self, string=""):
    return '\033[6m' + str(string) + self.close_string

  def flash(self, string=""):
    return '\033[5m' + str(string) + self.close_string  
  
  def underline(self, string=""):
    return '\033[4m' + str(string) + self.close_string
  
  def italic(self, string=""):
    return '\033[3m' + str(string) + self.close_string
  
  def bold(self, string=""):
    return '\033[1m' + str(string) + self.close_string


# Python Console Extensions
strColor = __strColor__()


class testSet:

  def __init__(self, file):
    self.logs = {
      'name': file.__name__,
      'path': file.__file__,
      'status': undefined,
      'tests': {
        'passing': [],
        'failing': [],
      },
      'warnings': [],
      'start-time': sysTime(),
      'end-time': undefined, 
    }
    self.failures = 0
    self.passes = 0

  def test(self, label,
    test=None, equals=undefined, 
    isNot=undefined, contains=undefined,
    arg=undefined):
    if test is None:
      test = label
      label = undefined
    if not isinstance(arg, tuple) and arg is not undefined:
      arg = (arg, )
    report_parameter = undefined
    R = {
      'name': str(test),
      'test': test,
      'passed': [],
      'failed': [],
      'result': undefined,
      'time-taken': 0
    }
    if label is not undefined:
      R['label'] = label
    if defined(arg) and len(arg) == 1: 
      R['type'] = str(arg[0])
    elif defined(arg):
      R['type'] = str(arg)
    test_start_time = sysTime()
    def run_test(arg, **kwargs):
      if callable(test):
        R['name'] = test.__name__
        try:
          if arg is not undefined:
            return test(*arg)
          else:
            return test()
        except Exception as e:
          return str(e)
      else:
        return test
    R['time-taken'] = sysTime()
    R['result'] = run_test(arg)
    R['time-taken'] = sysTime() - R['time-taken']
    
    # EQUALITY TEST
    if defined(equals):
      if R['result'] == equals:
        R['passed'].append( 
          { 
            'test': 'equals',
            'result': equals 
          }
        )
      else:
        R['failed'].append( 
          { 
            'test': 'expected', 
            'result': R['result'], 
            'expected': equals 
          } 
        )
    # IS NOT TEST
    if isNot is not undefined:
      if R['result'] is not isNot:
        R['passed'].append( 
          { 
            'test': 'is not',
            'result': isNot 
          }
        )
      else:
        R['failed'].append( 
          { 
            'test': 'is', 
            'result': R['result'],
            'expected': isNot
          } 
        )
    # CONTAINMENT TEST
    if contains is not undefined:
      if R['result'] in contains:
        R['passed'].append( 
          { 
            'test': 'contains',
            'result': contains 
          }
        )
      else:
        R['failed'].append( 
          { 
            'test': 'missing', 
            'result': R['result'], 
            'expected': contains 
          } 
        )
    if len(R['failed']) > 0:
      self.logs['tests']['failing'].append(R)
    else:
      self.logs['tests']['passing'].append(R)

  def count_passing(self):
    self.passes = 0
    for passed in self.logs['tests']['passing']:
      self.passes = self.passes + len(passed['passed'])

  def count_failures(self):
    self.failures = 0
    for failed in self.logs['tests']['failing']:
      self.failures = self.failures + len(failed['failed'])

  def log(self):
    self.logs['end-time'] = sysTime()
    _pad_ = "   "
    title = strColor.highlight(_pad_ + self.logs['name'] + _pad_ + _pad_)
    subtitle = strColor.black(self.logs['path'][-20:])
    if len(self.logs['path']) > 22: 
      subtitle = strColor.black("..") + strColor.black(self.logs['path'][-20:])
    else:
      subtitle = strColor.black(self.logs['path'])
    self.count_failures()
    self.count_passing()
    header = ""
    time = self.logs['end-time'] - self.logs['start-time']
    if self.failures > 0:
      prefix = ' '
      if self.failures > 1:
        prefix = 's'
      header = header + \
        strColor.red(title) + '\n' + \
        _pad_ + \
        subtitle + '\n' + \
        _pad_ + \
        strColor.red(strColor.blink('\u2023')) + ' ' + strColor.red(str(self.failures) + ' ' + 'failure' + prefix) + \
        "   "
    else:
      header = header + \
        strColor.green(title) + \
        '\n' + _pad_ + \
        subtitle + '\n' + \
        _pad_
    prefix = ''
    if self.passes > 1:
      prefix = 'es'
    passed_line = ' ' + 'pass' + prefix
    if self.failures > 0:
      header = header + strColor.black(str(self.passes) + passed_line)
    else: 
      header = header + strColor.green(_pad_ + '\u2714' + _pad_ + str(self.passes) + passed_line)
    header = header + '\n' + _pad_ + \
      strColor.black("spent  " + str(round(time, 13)) + "s")
    print(strColor.bold(header), '\n')
    for fail in self.logs['tests']['failing']:
      print(' ' + strColor.bold(strColor.red('\u0FBE ' + fail['name'])) + strColor.italic('( ' + strColor.black(fail['type']) + ' )'))
      if 'label' in fail:
        print(' ', strColor.red(fail['label']))
      for failed in fail['failed']:
        print(_pad_, strColor.red(str(failed['test']) + ' -> ' + str(failed['expected'])))
        print(_pad_, strColor.red('received -> ' + str(failed['result']) + '\n'))
    # if not _['crashed'] and len(_['passes']) > 0:
    #   if len(_['fails']) > 0:
    #     executed = strColor.red("     \u2023  ")
    #   else:
    #     executed = strColor.green("     \u0700  ")
    # else:
    #   executed = strColor.red("   \u16ED  ")
    # if len(_['fails']) > 0:
    #   executed = strColor.flash(executed)

    # parameters = str(_['parameters']).replace(',)', ')')
    # max_para_len = 32
    # if len(_['fails']) == 0:
    #   parameters = strColor.black("()")
    # elif len(parameters) >= max_para_len:
    #   parameters = parameters[:max_para_len] + strColor.black("...") + strColor.black(")")
    # _['parameters'] = parameters

    # test_title = executed
    # test_passes = []
    # test_fails = []

    # if not _['crashed']:
    #   for pas in _['passes']:
    #     if len(str(pas)) > 128:
    #       pas = deformat(pas).split('->')[0] + '-> ' + strColor.black('...')
    #     if len(str(pas)) > 64:
    #       pas = deformat(pas)[:48] + strColor.black('...')
    #     test_passes.append(strColor.green(u'       \u2714 ') + ' ' + str(pas))
    #   for fail in _['fails']:
    #     if len(str(fail)) > 128:
    #       fail = deformat(fail).split('->')[0] + '-> ' + strColor.black('...')
    #     if len(str(fail)) > 64:
    #       fail = deformat(fail)[:48] + strColor.black('...')
    #     test_fails.append(strColor.red(u'       \u0FBE ') + ' ' + str(fail) + strColor.red('\n        expected -> ') + _['log'])

    # if len(test_fails) == 0:
    #   if callable(_['function']):
    #     test_title = test_title + strColor.bold(strColor.black(str(_['function'].__name__) + parameters))
    #   else:
    #     test_title = test_title + strColor.bold(strColor.black(str(_['function']) + parameters))
    # else:
    #   test_title = test_title + strColor.bold(strColor.red(str(_['function'].__name__)) + parameters)

    # if callable(_['function']):
    #   log = _['function'].__name__ + _['parameters']
    # else:
    #   log = str(_['function']) + _['parameters']
    # if log in self.logs:
    #   for pas in test_passes:
    #     self.logs[log][1].append(pas)
    #   for fail in test_fails:
    #     self.logs[log][2].append(fail)
    # else:
    #   self.logs[log] = (test_title, test_passes, test_fails)


class newTests:
  sets = []

  def print(self):
    for log in self.test.logs:
      print(log)
  
  def file(self, file):
    self.sets.append(testSet(file))
    return self.sets[-1]


mock = newTests()


class __console__:

  def __init__(self, _input=None):
    if _input is not None:
      self.log(_input)
  
  def log(self, _input):
    _ = _console(_input)
    return _

  def clear(self):
    if sysOS == 'nt': 
        self.log('cls') 
    else: 
        self.log('clear') 


console = __console__()
