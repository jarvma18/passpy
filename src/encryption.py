def pad_for_aes256(plaintext: str) -> str:
  block_size = 16
  remainder = len(plaintext) % block_size
  padding_needed = block_size - remainder
  return plaintext + padding_needed * ' '

def unpad_for_aes256(plaintext: str) -> str:
  return plaintext.rstrip()