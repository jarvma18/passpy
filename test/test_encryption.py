import unittest

from src.encryption import AES256Cipher

class TestClass(unittest.TestCase):
  def test_should_pad_text_for_aes256(self):
    plaintext: str = 'test'
    expected_value: str = 'test\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'
    padded_text: str = AES256Cipher.pad(plaintext)
    self.assertEqual(expected_value, padded_text)

  def test_should_unpad_text(self):
    padded_text = 'test\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'.encode('utf-8')
    expected_value: str = 'test'
    plaintext: str = AES256Cipher.unpad(padded_text)
    self.assertEqual(expected_value, plaintext)

  def test_should_encrypt_text_to_aes256(self):
    text_to_encrypt: str = 'test'
    aes_256_cipher: str = AES256Cipher('test')
    encrypted_text: str = AES256Cipher.encrypt(aes_256_cipher, text_to_encrypt)
    self.assertNotEqual(text_to_encrypt, encrypted_text)

  def test_should_decrypt_text_to_aes256(self):
    text_to_encrypt: str = 'test'
    aes_256_cipher: str = AES256Cipher('test')
    encrypted_text: str = AES256Cipher.encrypt(aes_256_cipher, text_to_encrypt)
    decrypted_text: str = AES256Cipher.decrypt(aes_256_cipher, encrypted_text)
    self.assertNotEqual(encrypted_text, decrypted_text)

if __name__ == '__main__':
  unittest.main()