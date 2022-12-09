from decouple import config

"""
# This is a sample config file, to have a single point of configuration for your application.
# Python dependency: https://pypi.org/project/python-decouple/
# Order of precedence:
#   1. Environment variables
#   2. File .env
#   2. Default value: config('SQL_DB_SERVER', default='localhost')
"""
SQL_DB_SERVER = config('SQL_DB_SERVER', default='localhost')
SQL_DB_PORT = config('SQL_DB_PORT', default=3306)
SQL_DB_USER = config('SQL_DB_USER', default='root')
SQL_DB_PASSWORD = config('SQL_DB_PASSWORD')
SQL_DB_SCHEMA = config('SQL_DB_SCHEMA', default='python_test')

REDIS_DB_SERVER = config('REDIS_DB_SERVER', default='localhost')
REDIS_DB_PORT = config('REDIS_DB_PORT', default=6379)
REDIS_DB_NUMBER = config('REDIS_DB_NUMBER', default=0)

print(f'####################################')
print(f'{SQL_DB_SERVER=}')
print(f'{REDIS_DB_SERVER=}')
