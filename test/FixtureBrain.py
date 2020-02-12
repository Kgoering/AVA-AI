import unittest
import yaml
import sys

sys.path.append('../src')

import brain
from skills import Weather


class TestBrain(unittest.TestCase):
    def test_load_config_success(self):
        filename = '../config/config.yaml'
        config_data = brain.load_config(filename)

        with open(filename, 'r') as stream:
            yaml_data = yaml.load(stream, Loader=yaml.FullLoader)

            self.assertEqual(yaml_data, config_data)

    def test_load_config_fail(self):
        config_data = brain.load_config('')
        self.assertEqual({}, config_data)

    def test_load_mysql_success(self):
        config_data = brain.load_config('../config/config.yaml')

        db_conn = brain.load_mysql(config_data)
        self.assertIsNotNone(db_conn)

        db_conn.close()

    def test_load_mysql_fail(self):
        db_conn = brain.load_mysql({})
        self.assertIsNone(db_conn)

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

    def test_load_apis_success(self):
        api_calls = brain.load_apis([Weather.load_api])
        self.assertNotEqual(api_calls, [])
        self.assertEqual(api_calls[0][1], 'weather')

    def test_load_apis_fail(self):
        api_calls = brain.load_apis([])
        self.assertEqual(api_calls, [])


if __name__ == '__main__':
    unittest.main()
