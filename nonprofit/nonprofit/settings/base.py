import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

#-------------------------------------------------------------------------------
# Generic Django project settings
#-------------------------------------------------------------------------------

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Chris Pickett', 'chris.pickett@nerdery.com'),
    ('Sam Carlton', 'samuel.carlton@nerdery.com'),
)

MANAGERS = ADMINS

SITE_ID = 1

TIME_ZONE = 'America/Chicago'
USE_TZ = False
USE_I18N = True
USE_L10N = True

LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

SECRET_KEY = ')zeg!2d&tec.2(ch0t$o2=!s3_5$2+fi!hu&xmpptenb6m#0_x'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'south',
)

WSGI_APPLICATION = 'nonprofit.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, '../../vault.sqlite'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


#-------------------------------------------------------------------------------
# URL's and static/media/template settings
#-------------------------------------------------------------------------------

ROOT_URLCONF = 'nonprofit.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, '../static_files')
MEDIA_ROOT = os.path.join(PROJECT_DIR, '../media')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, '../static/'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, '../templates/'),
)

#-------------------------------------------------------------------------------
# Middleware
#-------------------------------------------------------------------------------

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#-------------------------------------------------------------------------------
# App settings
#-------------------------------------------------------------------------------
