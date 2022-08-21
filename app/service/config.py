import configparser
from distutils.command.config import config
config = configparser.RawConfigParser()
config.read("config.properties")

def get_app_hostname():
    return config.get("Database", "app_hostname")

def get_app_username():
    return config.get("Database", "app_username")

def get_app_password():
    return config.get("Database", "app_password")

def get_app_dbname():
    return config.get("Database", "app_dbname")