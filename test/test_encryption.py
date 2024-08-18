import unittest

from src.encryption import pad_for_aes256
from src.encryption import unpad_for_aes256
from src.encryption import encrypt_aes256
from src.encryption import decrypt_aes256

class TestClass(unittest.TestCase):
  def test_should_pad_text_for_aes256(self):
    plaintext: str = 'test'
    expected_value: str = 'test\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'
    padded_text: str = pad_for_aes256(plaintext)
    self.assertEqual(expected_value, padded_text)

  def test_should_unpad_text(self):
    padded_text = 'test\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'.encode('utf-8')
    expected_value: str = 'test'
    plaintext: str = unpad_for_aes256(padded_text)
    self.assertEqual(expected_value, plaintext)

  def test_should_encrypt_text_to_aes256(self):
    text_to_encrypt: str = 'test'
    key: str = 'test'
    encrypted_text: str = encrypt_aes256(text_to_encrypt, key)
    self.assertNotEqual(text_to_encrypt, encrypted_text)

  def test_should_decrypt_text_to_aes256(self):
    text_to_encrypt: str = 'test'
    key: str = 'test'
    encrypted_text: str = encrypt_aes256(text_to_encrypt, key)
    decrypted_text: str = decrypt_aes256(encrypted_text, key)
    self.assertNotEqual(encrypted_text, decrypted_text)

if __name__ == '__main__':
  unittest.main()