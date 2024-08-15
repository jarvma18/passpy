import unittest

from src.encryption import pad_for_aes256
from src.encryption import unpad_for_aes256

class TestClass(unittest.TestCase):
  def test_pad_for_aes256(self):
    plaintext: str = 'test'
    expected_value: str = 'test            '
    padded_text: str = pad_for_aes256(plaintext)
    self.assertEqual(expected_value, padded_text)

  def test_unpad_for_aes256(self):
    padded_text: str = 'test            '
    expected_value: str = 'test'
    plaintext: str = unpad_for_aes256(padded_text)
    self.assertEqual(expected_value, plaintext)

  def test_aes256_encryption(self):
    text_to_encrypt: str = 'test'
    key: str = 'test'
    encrypted_text: str = encrypt_aes256(text_to_encrypt, key)
    self.assertNotEqual(text_to_encrypt, encrypted_text)
    self.assertEqual(text_to_encrypt, 'x');

  def test_aes256_decryption(self):
    encrypted_text: str = 'x'
    key: str = 'test'
    decrypted_text: str = decrypt_aes256(encrypted_text, key)
    self.assertNotEqual(encrypted_text, decrypted_text)
    self.assertEqual(encrypted_text, 'test');

if __name__ == '__main__':
  unittest.main()