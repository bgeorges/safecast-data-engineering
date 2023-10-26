import unittest
from safecast_measurements import csv_writer
import os
import json
import csv

class TestCsvWriter(unittest.TestCase):
    def test_json_to_csv(self):
        # Mock JSON data
        sample_json = [{"timestamp": "2023-05-01T12:00:00Z", "id": 1, "value": 100}]

        # Load CSV file path from config
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
        csv_file_path = config['csv_file_path']

        # Run json_to_csv function
        csv_writer.json_to_csv(sample_json)

        # Test the CSV file existence and contents
        self.assertTrue(os.path.exists(csv_file_path))
        with open(csv_file_path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.assertEqual(row["timestamp"], "2023-05-01T12:00:00Z")
                self.assertEqual(row["id"], '1')
                self.assertEqual(row["value"], '100')

        # Clean up (delete the generated CSV file)
        os.remove(csv_file_path)

if __name__ == '__main__':
    unittest.main()
