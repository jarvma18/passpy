import unittest
import io
import sys

from src.file import read_file
from src.file import open_file

class TestClass(unittest.TestCase):
  def test_open_not_existing_file(self):
    exception_message: str = 'File not found, check that the file exists in that path'
    test_file: str = 'not_existing_file.txt'
    with self.assertRaises(Exception) as context:
      open_file(test_file)
    self.assertTrue(exception_message in str(context.exception))

  def test_read_file(self):
    test_file: str = 'test/test_file.json'
    expeted_value: str = '{"test": "test"}'
    read_file_content: str = read_file(test_file)
    self.assertEqual(expeted_value, read_file_content)

if __name__ == '__main__':
  unittest.main()