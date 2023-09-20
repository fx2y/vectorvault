import os
import tempfile
import unittest

from data_ingestion import FileSystemReader


class TestFileSystemReader(unittest.TestCase):
    def setUp(self):
        self.reader = FileSystemReader()

    def test_read_valid_file(self):
        # create temporary file with test data
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            f.write("name=John,age=30\n")
            f.write("name=Jane,age=25\n")
            filename = f.name

        # read data from file
        data = self.reader.read(f"file:{filename}")

        # check that data is correct
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], {"name": "John", "age": "30"})
        self.assertEqual(data[1], {"name": "Jane", "age": "25"})

        # delete temporary file
        os.remove(filename)

    def test_read_invalid_file(self):
        # read data from non-existent file
        with self.assertRaises(ValueError):
            self.reader.read("file:/path/to/nonexistent/file.txt")

        # read data from file with invalid format
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            f.write("invalid_format\n")
            filename = f.name
        with self.assertRaises(ValueError):
            self.reader.read(f"file:{filename}")
        os.remove(filename)

    def test_read_invalid_source(self):
        # read data from invalid source
        with self.assertRaises(ValueError):
            self.reader.read("invalid_source")


if __name__ == "__main__":
    unittest.main()
