from os import environ, mkdir, listdir
from shutil import rmtree
from fastapi_crudrouter import TortoiseCRUDRouter

DB_URL = environ.get('DB_URL', "sqlite://sql_app.db")
DOMAIN_BACKEND = environ.get('REACT_APP_DOMAIN_BACKEND', "http://localhost:8000")

TMP_DIR = 'TMP_DIR'

if TMP_DIR not in listdir():
    mkdir(TMP_DIR)
else:
    rmtree(TMP_DIR)
    mkdir(TMP_DIR)

CRUDRouter = TortoiseCRUDRouter


class DBPaths:
    base = ['db.base.models']

    users = ['db.users.models']

    project = ['db.project.models']

    all_paths = ["aerich.models"] + users + base + project


class MediaPath:
    path = f'static'

    @staticmethod
    def init_dirs():
        if MediaPath.path not in listdir():
            mkdir(MediaPath.path)

TORTOISE_ORM = {
    "connections": {"default": DB_URL},
    "apps": {
        "models": {
            "models": DBPaths.all_paths,
            "default_connection": "default",
        }
    },
}

MediaPath.init_dirs()

SECRET = "TkanfksdKASDlkasd"
LIFETIME_SESSION = None
