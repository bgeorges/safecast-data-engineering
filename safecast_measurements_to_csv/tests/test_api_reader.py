import unittest
from safecast_measurements import api_reader

class TestApiReader(unittest.TestCase):
    def test_fetch_data(self):
        test_url = "https://api.safecast.org/measurements.json"
        data = api_reader.fetch_data(test_url)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
