try:

  # Run All Tests
  from . import \
    _basic, _sqlmem, _reflask, \
    _server, _edoc, _etags, \
    _client, _comrade 

  # Tests to Log
  log = [
    _basic, _sqlmem, _reflask,
    _server, _edoc, _etags,
    _client, _comrade
  ]

  # Log Tests
  for test in log:
    try:
      test.file.log()
    except Exception as test_log_error:
      print(
        'Failed to log',
        test.__name__,
        '\n  error: ',
        test_log_error.with_traceback(test_log_error.__traceback__),
        '\n'
      )


except Exception as test_execution_error:
  print('Failed to execute tests:')
  
  if "object has no attribute '__name__'" in str(test_execution_error):
    print(
      "     ",
      "mock.file requires a imported python file",
      "\n     ",
      "but received",
      str(test_execution_error).split(" ")[0],
      "\n     ",
      "is this a .py file?"
    )
  
  else:
    print(
      '   ',
      test_execution_error.with_traceback(test_execution_error.__traceback__),
      '\n'
    )
    # RERUN TESTS FOR CRITICAL LOGGING
    from . import \
      _basic, _sqlmem, _reflask, \
      _server, _edoc, _etags, \
      _client, _comrade
