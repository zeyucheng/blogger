import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class Config:
    DEBUG = True
    SECRET_KEY = b'\x1dM\xb3\xaf1\x9b\xbbT>\x96*7\x10=5\xe6'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/blogger.db'.format(dir_path)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADS_DEFAULT_DEST = 'blogger/static/image'