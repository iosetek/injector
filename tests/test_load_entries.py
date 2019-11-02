import unittest
from entry_loader import EntryLoader
from entry import Entry

class TestLoadEntries(unittest.TestCase):
    def test_valid_entries_utf8(self):
        entries = EntryLoader.load_entries("tests/test_data/test_valid_entries_utf8.json")
        self.assertEqual(len(entries), 3)

        expected_keys = [
            bytearray("first sentence", "utf8"),
            bytearray("second sentence", "utf8"),
            bytearray("sentence with \"quotes\"", "utf8")
        ]
        expected_values = [
            bytearray("first translated sentence", "utf8"),
            bytearray("second translated sentence", "utf8"),
            bytearray("translation with special character\n", "utf8")
        ]
        
        for i in range(3):
            self.assertEqual(entries[i].key, expected_keys[i])
            self.assertEqual(entries[i].value, expected_values[i])


    def test_valid_entries_utf16(self):
        entries = EntryLoader.load_entries("tests/test_data/test_valid_entries_utf16.json")
        self.assertEqual(len(entries), 3)

        expected_keys = [
            bytearray("first sentence", "utf16")[2:],
            bytearray("second sentence", "utf16")[2:],
            bytearray("sentence with \"quotes\"", "utf16")[2:]
        ]

        expected_values = [
            bytearray("first translated sentence", "utf16")[2:],
            bytearray("second translated sentence", "utf16")[2:],
            bytearray("translation with special character\n", "utf16")[2:]
        ]
        
        for i in range(3):
            self.assertEqual(entries[i].key, expected_keys[i])
            self.assertEqual(entries[i].value, expected_values[i])
