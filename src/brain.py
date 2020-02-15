import yaml
import mysql.connector as mysql

from skills import Weather

# Globals
# Apis to load
api_list = [Weather.load_api]


def load_config(filename):
    try:
        with open(filename, 'r') as filestream:
            yaml_data = yaml.load(filestream, Loader=yaml.FullLoader)
            return yaml_data
    except FileNotFoundError:
        print("\nNo such config file")
        return {}


def load_mysql(db_login):
    try:
        db_conn = mysql.connect(
            host=db_login['dbhost'],
            user=db_login['user'],
            passwd=db_login['pass'],
            database=db_login['dtbs'])
        return db_conn
    except:
        return None


def load_user(db_conn, username):
    cursor = db_conn.cursor()
    username = username.lower()
    cursor.execute("SELECT * FROM users where name = '%s'" % username)
    data = cursor.fetchone()

    if not data:
        return (None, None)
    else:
        user = {'name': data[0].title()}
        return (user, data[1].title())


def load_ai(db_conn, ai_name):
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM ais where name = '%s'" % ai_name)
    data = cursor.fetchone()

    if not data:
        return None
    else:
        return {'name': data[0].title(), 'sex': data[1].title()}


def load_apis(apis):
    api_dict = []

    for api in apis:
        funct, keys = api()
        api_dict.append((funct, keys))

    return api_dict


def load(config_file):
    config_data = load_config(config_file)
    db_conn = load_mysql(config_data)
    # Ask for username
    username = "Kaleb"
    user, ai_name = load_user(db_conn, username)
    ai = load_ai(db_conn, ai_name)
    api_lookup = load_apis(api_list)
    return (db_conn, user, ai, api_lookup)
