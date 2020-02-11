import yaml


def load_config(filename):
    filestream = open(filename, 'r')
    yaml_data = yaml.load(filestream)
    return yaml_data
