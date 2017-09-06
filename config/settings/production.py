from .base import *

import json
'''
with open('secrets/prod_secrets.json') as f:
    secrets = json.loads(f.read())cd
    
def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)
'''
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'whb50d^$a$blw3nymfycq&8pizac+m5flrhr%28bw^p_z(5o*p"'

DEBUG = False

WHITENOISE_MIDDLEWARE = ['whitenoise.middleware.WhiteNoiseMiddleware', ]
MIDDLEWARE = WHITENOISE_MIDDLEWARE + MIDDLEWARE

INSTALLED_APPS += ['gunicorn', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'business_management_prod_db',
        'USER': 'business_management_prod_user',
        'PASSWORD': 'Rom.8:38-39PTL!',
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['127.0.0.1', 'cloud.digitalocean.com', 'digitalocean.com', 'corporate.optipulse.com', 'optipulse.com', 'localhost', '138.68.48.73',]