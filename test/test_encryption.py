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