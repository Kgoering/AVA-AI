import unittest
import yaml
import sys

sys.path.append('../src')

import brain


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

    def test_load_mysql(self):
        config_data = brain.load_config('../config/config.yaml')

        db_conn = brain.load_mysql(config_data)
        self.assertIsNotNone(db_conn)

    def test_load_user_success(self):
        config_data = brain.load_config('../config/config.yaml')
        db_conn = brain.load_mysql(config_data)

        user, ai_name = brain.load_user(db_conn, 'kaleb')
        self.assertIsNotNone(user)
        self.assertEqual(user['name'], 'kaleb')
        self.assertEqual(ai_name, 'ava')

    def test_load_user_fail(self):
        config_data = brain.load_config('../config/config.yaml')
        db_conn = brain.load_mysql(config_data)

        user, ai_name = brain.load_user(db_conn, 'lita')
        self.assertIsNone(user)
        self.assertIsNone(ai_name)

    def test_load_ai_success(self):
        config_data = brain.load_config('../config/config.yaml')
        db_conn = brain.load_mysql(config_data)

        ai = brain.load_ai('ava')
        self.assertIsNotNone(ai)
        self.assertEqual(ai['name'], 'ava')
        self.assertEqual(ai['sex'], 'F')


if __name__ == '__main__':
    unittest.main()
