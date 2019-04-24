import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KET") or "development"
