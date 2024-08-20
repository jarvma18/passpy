from file import read_file, write_file

class Storage:
  def __init__(self, path: str):
    self.path = path

  def read(self) -> str:
    return read_file(self.path)