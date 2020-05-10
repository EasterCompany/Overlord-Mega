try:

  # Run Tests
  from . import src

  # Log Tests
  src.elang.basic.file.log()
  src.elang.sqlmem.file.log()
  src.elang.reflask.file.log()

except Exception as test_execution_error:
  # Log Test Execution Errors
  print(test_execution_error)
