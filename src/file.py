from typing import TextIO

def open_file(file_name: str) -> TextIO:
  try:
    file = open(file_name, 'r')
  except FileNotFoundError:
    raise Exception('File not found, check that the file exists in that path')
  else:
    return file

def read_file(file_name: str) -> str:
  file = open_file(file_name)
  if file:
    file_content: str = file.read()
    file.close()
    return file_content
  else:
    return