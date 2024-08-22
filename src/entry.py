import json
import uuid

from src.storage import Storage

class Entry:
  def __init__(self, storage: Storage, data: dict):
    self.storage = storage
    self.data = data

  def add(self, username, password):
    entry_id = uuid.uuid4()
    self.data[str(entry_id)] = {'username': username, 'password': password}
    self.storage.write(json.dumps(self.data))

  def read(self, entry_id):
    return self.data[entry_id]
  
  def delete(self, entry_id):
    del self.data[entry_id]
    self.storage.write(json.dumps(self.data))
  
  def update(self, entry_id, username, password):
    self.data[entry_id] = {'username': username, 'password': password}
    self.storage.write(json.dumps(self.data))