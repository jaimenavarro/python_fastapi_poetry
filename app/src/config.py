from decouple import config

"""
# This is a sample config file, which should be committed to your repo.
# Python dependency: https://pypi.org/project/python-decouple/
"""
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
