from os.path import dirname, abspath
from os import environ

class Settings(object):
    PROJECT_ROOT = dirname(abspath(__file__))

    def __init__(self) -> None:
        environ['PYTHONDONTWRITEBYTECODE'] = '1'
        environ['PYTHONUNBUFFERED'] = '1'

proj_settings=Settings()
