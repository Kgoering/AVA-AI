import yaml


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
