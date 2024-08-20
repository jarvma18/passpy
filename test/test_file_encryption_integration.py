import unittest
import os

from src.file import read_file
from src.file import write_file
from src.encryption import AES256Cipher
from test.shared import delete_file

class TestClass(unittest.TestCase):
  test_file: str = 'test/test_file_encrypted.json'
  test_file_content: str = '{"test": "test"}'
  aes_256_cipher: str = AES256Cipher('test')

  def test_should_create_file_and_encrypt_and_decrypt_content(self):
    encrypted_content: str = AES256Cipher.encrypt(self.aes_256_cipher, self.test_file_content)
    write_file(self.test_file, encrypted_content)
    encrypted_file_content: str = read_file(self.test_file)
    self.assertNotEqual(self.test_file_content, encrypted_file_content)
    decrypted_file_content: str = AES256Cipher.decrypt(self.aes_256_cipher, encrypted_file_content)
    self.assertEqual(self.test_file_content, decrypted_file_content)
    delete_file(self)