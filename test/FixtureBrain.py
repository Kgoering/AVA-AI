import unittest
import yaml
import sys

sys.path.append('../src')

import brain


class TestBrain(unittest.TestCase):
    def test_load_config(self):
        filename = '../config/config.yaml'
        config_data = brain.load_config(filename)

        with open(filename, 'r') as stream:
            yaml_data = yaml.load(stream, Loader=yaml.FullLoader)

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

        db_conn.close()

    def test_load_user_success(self):
        config_data = brain.load_config('../config/config.yaml')
        db_conn = brain.load_mysql(config_data)

        user, ai_name = brain.load_user(db_conn, 'kaleb')
        self.assertIsNotNone(user)
        self.assertEqual(user['name'], 'Kaleb')
        self.assertEqual(ai_name, 'Ava')

        db_conn.close()

    def test_load_user_fail(self):
        config_data = brain.load_config('../config/config.yaml')
        db_conn = brain.load_mysql(config_data)

        user, ai_name = brain.load_user(db_conn, 'lita')
        self.assertIsNone(user)
        self.assertIsNone(ai_name)

        db_conn.close()

    def test_load_ai_success(self):
        config_data = brain.load_config('../config/config.yaml')
        db_conn = brain.load_mysql(config_data)

        ai = brain.load_ai(db_conn, 'ava')
        self.assertIsNotNone(ai)
        self.assertEqual(ai['name'], 'Ava')
        self.assertEqual(ai['sex'], 'F')

        db_conn.close()

    def test_load_ai_fail(self):
        config_data = brain.load_config('../config/config.yaml')
        db_conn = brain.load_mysql(config_data)

        ai = brain.load_ai(db_conn, 'lita')
        self.assertIsNone(ai)

        db_conn.close()

    def test_load_apis_fail(self):
        api_calls = brain.load_apis()
        self.assertEqual(api_calls, [])


if __name__ == '__main__':
    unittest.main()
