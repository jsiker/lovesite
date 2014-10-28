"""
Django settings for love project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h@83tw@pdp9qqu#8gw@7)%=r!#!z#k)!&(0yh1g4bbfmvz)k#!'

#######POSTMAN
POSTMAN_AUTO_MODERATE_AS = True

#####STRIPE
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "xxxxxxx")
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "xxxxxxx")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'squish',
    'payments',
    'debug_toolbar',
    # 'postman',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django_messages.context_processors.inbox',
# )

ROOT_URLCONF = 'love.urls'

WSGI_APPLICATION = 'love.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# register stuff
LOGIN_REDIRECT_URL = 'profile'
LOGIN_URL = 'login'  # given the string of login url page
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'jon.siker@gmail.com'
# EMAIL_HOST_PASSWORD = 'xxxxxxxx'
# EMAIL_PORT = 587
# DEFAULT_FROM_EMAIL = 'jon.siker@gmail.com'
# AUTH_USER_MODEL = 'squish.User'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static", *MEDIA_URL.strip("/").split("/"))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = ('/Users/danielsiker/projects/love/squish/static/',)
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
# Template location
# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, "templates"),
# )



try:
    from local_settings import *
except ImportError:
    pass
