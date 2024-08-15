import unittest

from src.file import read_file
from src.file import open_file
from src.file import handle_file_exception
from src.file import write_file

class TestClass(unittest.TestCase):
  def test_should_raise_exception_when_opening_not_existing_file(self):
    exception_message: str = 'File not found, check that the file exists in that path'
    test_file: str = 'not_existing_file.txt'
    with self.assertRaises(Exception) as context:
      open_file(test_file, 'r')
    self.assertTrue(exception_message in str(context.exception))

  def test_should_read_file(self):
    test_file: str = 'test/test_file.json'
    expeted_value: str = '{"test": "test"}'
    read_file_content: str = read_file(test_file)
    self.assertEqual(expeted_value, read_file_content)

  def test_should_handle_read_file_exception(self):
    exception_message: str = 'Error reading file: test'
    with self.assertRaises(Exception) as context:
      handle_file_exception(Exception('test'), 'read')
    self.assertTrue(exception_message in str(context.exception))

  def test_should_handle_write_file_exception(self):
    exception_message: str = 'Error writing to file: test'
    with self.assertRaises(Exception) as context:
      handle_file_exception(Exception('test'), 'write')
    self.assertTrue(exception_message in str(context.exception))

  def test_should_handle_file_exception_default(self):
    exception_message: str = 'Error handling file: test'
    with self.assertRaises(Exception) as context:
      handle_file_exception(Exception('test'), 'default')
    self.assertTrue(exception_message in str(context.exception))

  def test_should_write_file(self):
    test_file: str = 'test/test_file.json'
    content: str = '{"test": "test"}'
    write_file(test_file, content)
    read_file_content: str = read_file(test_file)
    self.assertEqual(content, read_file_content)

if __name__ == '__main__':
  unittest.main()