import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', os.path.join(os.getcwd(), 'uploads'))
    _db_url = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    if _db_url.startswith('postgresql://') and 'connect_timeout=' not in _db_url:
        _db_url = _db_url + ('&' if '?' in _db_url else '?') + 'connect_timeout=2'

    SQLALCHEMY_DATABASE_URI = _db_url or ('sqlite:///' + os.path.join(os.getcwd(), 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    SQLALCHEMY_ENGINE_OPTIONS = (
        {"connect_args": {"connect_timeout": 2}}
        if SQLALCHEMY_DATABASE_URI.startswith("postgresql://")
        else {}
    )
