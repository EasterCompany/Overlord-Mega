from platform import uname
from os import system as _console, \
  mkdir as mkDir
from . import path, pyExe, openUrl, \
  sysTime, sysOS


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


# Python Console Extension module
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


# Python Pip Module Installation
def __install__(__testfunction__=False):
  if __testfunction__:
    try:
      from flask import Flask
    except:
      return False
    return True
  else:
    console.log(path.realpath(pyExe) + " -m pip install --upgrade pip")
    console.log(path.realpath(pyExe) + " -m pip install --upgrade flask")


# Git Pull Command Function
def __gitUpdate__(__testfunction__=False):
  if __testfunction__:
    return path.exists('./.git')
  console.log("git pull")


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
      string = string.replace("  ", " ")
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


class __testFile__:

  def __init__(self, file):
    self.logs = {
      'name': file.__name__,
      'path': file.__file__,
      'status': undefined,
      'tests': { 'passing': [], 'failing': [], },
      'warnings': [],
      'start-time': sysTime(),
      'end-time': undefined,
    }
    self.failures = 0
    self.passes = 0

  def test(self, label, test=None, equals=undefined, isNot=undefined,
  contains=undefined, notContains=undefined, arg=undefined):
    
    # Adjust parameters for lazy programmers
    if test is None:
      test = label
      label = undefined
    
    # Adjust parameters for careless programmers
    if not isinstance(arg, tuple) and arg is not undefined:
      arg = (arg, )
    report_parameter = undefined
    
    # Define the test object
    R = {
      'name': str(test),
      'test': test,
      'passed': [],
      'failed': [],
      'result': undefined,
      'time-taken': 0
    }

    # Define the test type
    if label is not undefined:
      R['label'] = label
    if defined(arg) and len(arg) == 1: 
      R['type'] = str(arg[0])
    elif defined(arg):
      R['type'] = str(arg)
    test_start_time = sysTime()
    
    # Define the test environment
    def run_test(arg, **kwargs):
      run_result = undefined
      if callable(test):
        R['name'] = test.__name__
        try:
          if arg is not undefined:
            run_result = test(*arg)
          else:
            run_result = test()
          R['passed'].append( 
            { 
              'test': 'execution',
              'result': run_result 
            }
          )
        except Exception as e:
          R['failed'].append( 
            { 
              'test': 'execution', 
              'result': str(e),
              'expected': "a clean execution"
            } 
          )
          run_result = str(e)
      else:
        run_result = test
      return run_result
    
    # Log environment result
    R['time-taken'] = sysTime()
    R['result'] = run_test(arg)
    R['time-taken'] = sysTime() - R['time-taken']
    
    # EQUALITY TEST
    if equals is not undefined:
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
      if contains in R['result']:
        R['passed'].append( 
          { 
            'test': 'contains',
            'result': contains 
          }
        )
      else:
        contains_result = R['result']
        if not isinstance(R['result'], str):
          try:
            contains_result = []
            for x in R['result']:
              contains_result.append(x)
          except Exception as e:
            print('TE failed to parse -> contains ->', type(), e)
        R['failed'].append( 
          { 
            'test': 'missing', 
            'result': contains_result,
            'expected': contains
          } 
        )
    
    # VOID CONTAINMENT TEST
    if notContains is not undefined:
      if notContains not in R['result']:
        R['passed'].append( 
          { 
            'test': "doesn't contain",
            'result': notContains 
          }
        )
      else:
        notContains_result = R['result']
        if not isinstance(R['result'], str):
          try:
            notContains_result = []
            for x in R['result']:
              notContains_result.append(x)
          except Exception as e:
            print('TE failed to parse -> contains ->', type(), e)
        R['failed'].append( 
          { 
            'test': 'has', 
            'result': notContains_result,
            'expected': notContains 
          } 
        )
    
    # CATEGORY TEST
    if len(R['failed']) > 0:
      self.logs['tests']['failing'].append(R)
    else:
      self.logs['tests']['passing'].append(R)

  def count_passing(self):
    self.passes = 0
    for passed in self.logs['tests']['passing']:
      self.passes += len(passed['passed'])

  def count_failures(self):
    self.failures = 0
    for failed in self.logs['tests']['failing']:
      self.failures += len(failed['failed'])

  def log(self):
    # Console print styling
    self.logs['end-time'] = sysTime()
    _pad_ = "   "
    title = strColor.highlight(_pad_ + str(self.logs['name']) + _pad_ + _pad_)
    subtitle = strColor.black(self.logs['path'][-20:])
    
    # Stylise path to file
    if len(self.logs['path']) > 22: 
      subtitle = strColor.black("..") + strColor.black(self.logs['path'][-20:])
    else:
      subtitle = strColor.black(str(self.logs['path']))
    
    # Count total test conditions passed or failed
    self.count_failures()
    self.count_passing()
    
    # Define test header and time taken
    header = ""
    time = self.logs['end-time'] - self.logs['start-time']
    
    # When a test fail
    if self.failures > 0:
      prefix = ' '
      failed_line = strColor.red(strColor.blink('\u2023')) + ' '
      if self.passes == 0:
        failed_line = '   ' + failed_line + '  '
      failed_line = failed_line + strColor.red(str(self.failures) + ' ' + 'failure' + prefix)
      # When tests fail
      if self.failures > 1:
        prefix = 's'
      header = header + \
        strColor.red(title) + '\n' + \
        _pad_ + \
        subtitle + '\n' + \
        _pad_ + \
        failed_line + \
        "   "
    
    # When a test pass
    else:
      header = header + \
        strColor.green(title) + \
        '\n' + _pad_ + \
        subtitle + '\n' + \
        _pad_
    
    # Build console output
    prefix = ''
    if self.passes > 0:
      if self.passes > 1:
        prefix = 'ed'
      passed_line = str(self.passes) + ' ' + 'pass' + prefix
    else:
      passed_line = ' '

    if self.failures > 0:
      header = header + strColor.black(passed_line) + '\n' + _pad_
    
    elif self.passes > 0: 
      header = header + strColor.green(_pad_ + '\u2714' + _pad_ + passed_line) + '\n' + _pad_
    header = header + \
      strColor.black("spent  " + str(round(time, 13)) + "s")
    
    print(strColor.bold(header), '\n')
    
    for fail in self.logs['tests']['failing']:
    
      _line = ' ' + strColor.bold(strColor.red('\u0FBE ' + fail['name']))
      if 'type' in fail:
        _line += strColor.italic('( ' + strColor.black(str(fail['type'])) + ' )')
      print(_line)

      if 'label' in fail:
        print(' ', strColor.red(str(fail['label'])))
      for failed in fail['failed']:
        print(_pad_, strColor.red(str(failed['test']) + ' -> ' + str(failed['expected'])))
        print(_pad_, strColor.red('received -> ' + str(failed['result']) + '\n'))


class __testModule__:
  sets = []

  def print(self):
    for log in self.test.logs:
      print(log)
  
  def file(self, file):
    self.sets.append(__testFile__(file))
    return self.sets[-1]


mock = __testModule__()
