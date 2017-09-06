import dj_database_url

from .base import *


DEBUG = False

ALLOWED_HOSTS = ['*']

MIDDLEWARE = MIDDLEWARE + [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES['default'] =  dj_database_url.config()
