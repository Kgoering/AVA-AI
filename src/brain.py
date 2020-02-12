import yaml
import mysql.connector as mysql

# Globals
# Apis to load
apis = []


def load_config(filename):
    filestream = open(filename, 'r')
    yaml_data = yaml.load(filestream)
    return yaml_data


def load_mysql(db_login):
    db_conn = mysql.connect(
        host=db_login['dbhost'],
        user=db_login['user'],
        passwd=db_login['pass'],
        database=db_login['dtbs'])
    return db_conn


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


def load_apis():
    api_dict = []

    for api in apis:
        funct, keys = api()
        api_dict.append((funct, keys))

    return api_dict
