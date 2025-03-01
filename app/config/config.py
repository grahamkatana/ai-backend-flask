import os
from datetime import timedelta
from dotenv import load_dotenv
from app.utils.database_connector import get_connection_string

load_dotenv()


FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
SECRET_KEY = os.environ.get("SECRET_KEY")
ENV = os.environ.get("ENV")

FLASK_APP = os.environ.get("FLASK_APP")


SQLALCHEMY_DATABASE_URI = get_connection_string()
SQLALCHEMY_TRACK_MODIFICATIONS = False

BACKUP_DRIVE = os.environ.get("GOOGLE_PARENT_ID")

# secret key
JWT_SECRET_KEY = os.environ.get("SECRET_KEY")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2160)

# mail configuration
MAIL_SERVER = os.environ.get("EMAIL_SERVER")
MAIL_PORT = os.environ.get("EMAIL_PORT")
MAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
MAIL_USE_TLS = True if os.environ.get("EMAIL_USE_TLS") == "True" else False
MAIL_USE_SSL = True if os.environ.get("EMAIL_USE_SSL") == "True" else False

# file uploads config
UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER")
# 16 mb as max size set
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
FLASK_ADMIN_FLUID_LAYOUT = True
