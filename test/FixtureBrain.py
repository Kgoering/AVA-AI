import unittest
import yaml

from ..src import brain


class TestBrain(unittest.TestCase):
    def test_load_config(self):
        filename = '../config/config.yaml'
        config_data = brain.load_config(filename)

        stream = open(filename, 'r')
        yaml_data = yaml.load(stream)

        self.assertEqual(config_data['user'], yaml_data['user'])
        self.assertEqual(config_data['pass'], yaml_data['pass'])
        self.assertEqual(config_data['dbhost'], yaml_data['dbhost'])
        self.assertEqual(config_data['dtbs'], yaml_data['dtbs'])
        self.assertEqual(config_data['sthost'], yaml_data['sthost'])
        self.assertEqual(config_data['port'], yaml_data['port'])


if __name__ == '__main__':
    unittest.main()
