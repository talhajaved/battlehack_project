import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '1902095766682336',
        'secret': 'cb846832e14382f2b48788d8f3f98f4e'
    },
    'twitter': {
        'id': '4RZoVu6QFBsJGlU242bxMkqjb',
        'secret': 'rwLWS4QbK5ccpThaRwctiNZKL1VFqocTgqhGCeWd1VwPek4A4m'
    }
}

