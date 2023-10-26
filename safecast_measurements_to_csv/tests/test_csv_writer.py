import unittest
from safecast_measurements import csv_writer
import os
import csv

class TestCsvWriter(unittest.TestCase):
    def test_json_to_csv(self):
        sample_json = [{"timestamp": "2023-05-01T12:00:00Z", "id": 1, "value": 100}]
        csv_writer.json_to_csv(sample_json, "test.csv")

        self.assertTrue(os.path.exists("test.csv"))
        with open("test.csv", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.assertEqual(row["timestamp"], "2023-05-01T12:00:00Z")
                self.assertEqual(row["id"], '1')
                self.assertEqual(row["value"], '100')
        os.remove("test.csv")

if __name__ == '__main__':
    unittest.main()
