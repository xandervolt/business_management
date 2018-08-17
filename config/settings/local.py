from .base import *  # noqa

import json

with open('secrets/dev_secrets.json') as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exceptions'''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1', ]

DATABASES = {
    'default': {
        'ENGINE': get_secret('DATABASES_ENGINE'),
        'NAME': get_secret('DATABASES_NAME'),
        'USER': get_secret('DATABASES_USER'),
        'PASSWORD': get_secret('DATABASES_PASSWORD'),
        'HOST': get_secret('DATABASES_HOST'),
        'PORT': get_secret('PORT'),
    }
}

# Static File Configuration
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
MEDIA_ROOT = str(ROOT_DIR('media'))
MEDIA_URL = '/media/'
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]

ALLOWED_HOSTS = ['*']
