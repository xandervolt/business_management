# settings/base.py

"""
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import environ

ROOT_DIR = environ.Path(__file__) - 3  # (business_management/config/settings/base.py - 3 = business_management/)
APPS_DIR = ROOT_DIR.path('business_management')

# Load operating system environment variables and then prepare to use them
env = environ.Env()

# .env file, should load only in development environment
READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)

if READ_DOT_ENV_FILE:
    # Operating System Environment variables have precedence over variables defined in the .env file,
    # that is to say variables from the .env files will only be used if not defined
    # as environment variables.
    env_file = str(ROOT_DIR.path('.env'))
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
    print('The .env file has been loaded. See base.py for more information')


# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)


# Application definition
# ------------------------------------------------------------------------------

INSTALLED_APPS = [
    'admin_view_permission',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth_office365',
    #'social.apps.django_app.default',
    'reversion',
    
    'bootstrap4',
    
    'business_management.accounts',
    'business_management.engineering',
    'business_management.dashboard',
]

#SOCIALACCOUNT_ADAPTER = 'allauth_office365.adapter.SocialAccountAdapter'
SOCIALACCOUNT_EMAIL_VERIFICATION = False

SOCIALACCOUNT_PROVIDERS = {
    'office365': {
      'SCOPE': ['User.read',
                'Files.ReadWrite',
                ],
      'USERNAME_FIELD': 'mail'
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
]

ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    # for Office365/SharePoint Auth
    #'oauth.backends.AzureADOAuth2',
)


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# OAuth Office365/SharePoint Variables
# ------------------------------------------------------------------------------
'''
SOCIAL_AUTH_AZUREAD_OAUTH2_KEY = 'Your AzureAD Client ID'

SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET = 'Your AzureAD Secret'

SOCIAL_AUTH_AZUREAD_OAUTH2_RESOURCE = 'https://{YourSharepointTenant}.sharepoint.com'

SOCIAL_AUTH_AZUREAD_OAUTH2_SCOPE = ['Files.ReadWrite',]

SHAREPOINT_RESOURCE = 'https://optipulse.sharepoint.com'
'''

# AllAuth Settings
# ------------------------------------------------------------------------------

AUTH_USER_MODEL = 'accounts.User'

SITE_ID = 1

LOGIN_REDIRECT_URL = 'dashboard:dashboard'
ACCOUNT_EMAIL_REQUIRED = True # email required to signup
ACCOUNT_EMAIL_VERIFICATION = False # email verification manditory for account verification
ACCOUNT_AUTHENTICATION_METHOD = "username_email" # username or email
#ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
#VERIFIED_EMAIL = True
#ACCOUNT_FORMS = {'login': 'accounts.forms.MyLoginForm', 'sign_up': 'accounts.forms.MySignupForm'}
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
#ACCOUNT_SIGNUP_FORM_CLASS = 'business_management.accounts.forms.UserCreateForm'
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
#ACCOUNT_SESSION_REMEMBER = None # Controls the life time of the session. Set to None to ask the user 'Remember me?', False to not remember, and True to always remember.