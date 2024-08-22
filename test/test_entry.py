import unittest

from src.entry import Entry
from src.storage import Storage
from test.shared import delete_file

class TestClass(unittest.TestCase):
  test_file: str = 'test/test_entry_encrypted.json'
  storage: Storage = Storage(test_file, 'test')

  def test_should_create_entry(self):
    entry = Entry(None, {})
    self.assertIsNotNone(entry)

  def test_should_add_entry(self):
    entry = Entry(self.storage, {})
    entry.add('test', 'test')
    self.assertEqual(len(entry.data), 1)
    delete_file(self)

  def test_should_read_entry(self):
    entry = Entry(self.storage, {'test': {'username': 'test', 'password': 'test'}})
    entry_data = entry.read('test')
    self.assertEqual(entry_data, {'username': 'test', 'password': 'test'})

  def test_should_delete_entry(self):
    entry = Entry(self.storage, {'test': {'username': 'test', 'password': 'test'}})
    entry.delete('test')
    self.assertEqual(len(entry.data), 0)
    self.assertNotIn('test', entry.data)
    delete_file(self)

  def test_should_update_entry(self):
    entry = Entry(self.storage, {'test': {'username': 'test', 'password': 'test'}})
    entry.update('test', 'new_test', 'new_test')
    self.assertEqual(len(entry.data), 1)
    self.assertEqual(entry.data['test'], {'username': 'new_test', 'password': 'new_test'})
    delete_file(self)

if __name__ == '__main__':
  unittest.main()