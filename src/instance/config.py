import os

DATABASE_BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
    "sqlite:///" + os.path.join(DATABASE_BASE_DIR, "db")
SQLALCHEMY_TRACK_MODIFICATIONS=False
