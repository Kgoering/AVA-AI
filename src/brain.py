import yaml
import mysql.connector as mysql


def load_config(filename):
    filestream = open(filename, 'r')
    yaml_data = yaml.load(filestream)
    return yaml_data


def load_mysql(db_login):
    conn = mysql.connect(
        host=db_login['dbhost'],
        user=db_login['user'],
        passwd=db_login['pass'],
        database=db_login['dtbs'])
    return conn


def load_user(db_conn, username):
    cursor = conn.cursor()
    username = username.lower()
    cursor.execute("SELECT * FROM users where name = '%s'" % username)
    data = cursor.fetchone()

    if not data:
        return (None, None)
    else:
        user = {'name': data[0].title()}
        return (user, data[1].title())
