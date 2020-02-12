import unittest
import sys

sys.path.append('../src/skills')

import Weather


class TestWeather(unittest.TestCase):
    def test_load_api(self):
        func, keys = Weather.load_api()
        self.assertEqual(keys, "weather")

    def test_main(self):
        ret_str = Weather.main()
        self.assertEqual(ret_str, "Weather")


if __name__ == '__main__':
    unittest.main()
