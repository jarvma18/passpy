from typing import TextIO

def handle_file_exception(exception: Exception, operation: str) -> None:
  if operation == 'read':
    raise Exception(f'Error reading file: {str(exception)}')
  elif operation == 'write':
    raise Exception(f'Error writing to file: {str(exception)}')
  else:
    raise Exception(f'Error handling file: {str(exception)}')

def open_file(file_name: str, operation: str) -> TextIO:
  try:
    file = open(file_name, operation)
  except FileNotFoundError:
    raise Exception('File not found, check that the file exists in that path')
  else:
    return file

def read_file(file_name: str) -> str:
  try:
    with open_file(file_name, 'r') as file:
      file_content: str = file.read()
      return file_content
  except Exception as e:
    handle_file_exception(e, 'read')

def write_file(file_name: str, content: str) -> None:
  try:
    file = open_file(file_name, 'w')
    if file:
      file.write(content)
  except Exception as e:
    handle_file_exception(e, 'write')
  finally:
    if file:
      file.close()