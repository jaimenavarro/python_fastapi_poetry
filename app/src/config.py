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
REDIS_DB_SERVER = config('REDIS_DB_SERVER', default='localhost')

print(f'####################################')
print(f'{SQL_DB_SERVER=}')
print(f'{REDIS_DB_SERVER=}')