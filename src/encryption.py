import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import os

def pad_for_aes256(plaintext: str) -> str:
  block_size = 16
  remainder = len(plaintext) % block_size
  padding_needed = block_size - remainder
  return plaintext + padding_needed * ' '

def unpad_for_aes256(plaintext: str) -> str:
  return plaintext.rstrip()

def encrypt_aes256(text: str, key: str) -> str:
  initialization_vector: bytes = Random.new().read(AES.block_size)
  cipher = AES.new(key, AES.MODE_CBC, initialization_vector)
  padded_text: str = pad_for_aes256(text)
  encrypted_text: str = cipher.encrypt(padded_text)
  return base64.b64encode(initialization_vector + encrypted_text).decode()

def decrypt_aes256(encrypted_text: str, key: str) -> str:
  encrypted_text: str = base64.b64decode(encrypted_text)
  initialization_vector: bytes = encrypted_text[:AES.block_size]
  cipher = AES.new(key, AES.MODE_CBC, initialization_vector)
  decrypted_text: str = cipher.decrypt(encrypted_text[AES.block_size:])
  return unpad_for_aes256(decrypted_text.decode())