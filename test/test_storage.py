import unittest
import os

from src.storage import Storage
from test.shared import delete_file

class TestClass(unittest.TestCase):
  test_file: str = 'test/test_file_encrypted.json'
  test_file_content: str = '{"test": "test"}'
  storage: Storage = Storage(test_file, 'test')

  def test_should_create_file_and_encrypt_and_decrypt_content(self):
    self.storage.write(self.test_file_content)
    encrypted_file_content: str = self.storage.read()
    self.assertEqual(self.test_file_content, encrypted_file_content)
    delete_file(self)

  def test_should_not_be_able_to_decrypt_file_with_wrong_key(self):
    self.storage.write(self.test_file_content)
    storage_with_wrong_key: Storage = Storage(self.test_file, 'wrong_key')
    encrypted_file_content: str = storage_with_wrong_key.read()
    self.assertNotEqual(self.test_file_content, encrypted_file_content)
    delete_file(self)