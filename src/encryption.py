import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import os

def pad_for_aes256(plaintext: str) -> str:
  block_size = 16
  remainder = len(plaintext) % block_size
  padding = block_size - remainder
  return plaintext + chr(padding) * padding

def unpad_for_aes256(plaintext: bytes) -> str:
  padding = plaintext[-1]
  return plaintext[:-padding].decode('utf-8')

def encrypt_aes256(text: str, key: str) -> str:
  private_key: str = hashlib.sha256(key.encode("utf-8")).digest()
  raw_text: bytes = str.encode(pad_for_aes256(text))
  initialization_vector: bytes = Random.new().read(16)
  cipher = AES.new(private_key, AES.MODE_CBC, initialization_vector)
  encrypted_text: str = cipher.encrypt(raw_text)
  return base64.b64encode(initialization_vector + encrypted_text).decode()

def decrypt_aes256(encrypted_text: str, key: str) -> str:
  private_key = hashlib.sha256(key.encode("utf-8")).digest()
  encrypted_text: str = base64.b64decode(encrypted_text)
  initialization_vector: bytes = encrypted_text[:16]
  cipher = AES.new(private_key, AES.MODE_CBC, initialization_vector)
  decrypted_text: str = cipher.decrypt(encrypted_text[16:])
  return unpad_for_aes256(decrypted_text)