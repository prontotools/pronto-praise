import dj_database_url

from .base import *


# WhiteNoise won't work on Heroku when we set DEBUG = False
DEBUG = True

ALLOWED_HOSTS = ['*']

MIDDLEWARE = MIDDLEWARE + [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES['default'] =  dj_database_url.config()
