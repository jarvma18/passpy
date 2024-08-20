import os

def delete_file(self) -> None:
  if os.path.exists(self.test_file):
    os.remove(self.test_file)