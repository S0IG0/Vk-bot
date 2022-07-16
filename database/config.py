import os
from config_env import create_variables_in_environment
create_variables_in_environment()


host = os.environ.get('host')
user = os.environ.get('user')
password = os.environ.get('password')
database_name = os.environ.get('database_name')
port = os.environ.get('port')
