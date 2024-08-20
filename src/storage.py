from src.file import read_file, write_file
from src.encryption import AES256Cipher

class Storage:
  def __init__(self, path: str, key: str):
    self.path = path
    self.cipher = AES256Cipher(key)

  def read(self) -> str:
    encrypted_content = read_file(self.path)
    decrypted_content = self.cipher.decrypt(encrypted_content)
    return decrypted_content

  def write(self, content: str) -> None:
    encrypted_content = self.cipher.encrypt(content)
    write_file(self.path, encrypted_content)