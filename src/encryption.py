import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

class AES256Cipher:
  def __init__(self, key: str):
    self.key = hashlib.sha256(key.encode("utf-8")).digest()

  @staticmethod
  def pad(plaintext: str) -> str:
    block_size = 16
    remainder = len(plaintext) % block_size
    padding = block_size - remainder
    return plaintext + chr(padding) * padding

  @staticmethod
  def unpad(plaintext: bytes) -> str:
    padding = plaintext[-1]
    return plaintext[:-padding].decode('utf-8')

  def encrypt(self, text: str) -> str:
    raw_text: bytes = str.encode(AES256Cipher.pad(text))
    initialization_vector: bytes = Random.new().read(16)
    cipher = AES.new(self.key, AES.MODE_CBC, initialization_vector)
    encrypted_text: str = cipher.encrypt(raw_text)
    return base64.b64encode(initialization_vector + encrypted_text).decode()

  def decrypt(self, encrypted_text: str) -> str:
    encrypted_text: str = base64.b64decode(encrypted_text)
    initialization_vector: bytes = encrypted_text[:16]
    cipher = AES.new(self.key, AES.MODE_CBC, initialization_vector)
    decrypted_text: str = cipher.decrypt(encrypted_text[16:])
    return AES256Cipher.unpad(decrypted_text)