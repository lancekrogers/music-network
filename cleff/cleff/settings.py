"""
Django settings for cleff project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l^*dx&83(z(mxp5l7_8h8v4z3%vm9^#3&69li987h16v&qe^4x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_PROFILE_MODULE = "profiles.models.ProfileModel"



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'Forum',
    'profiles',
    'cleff_main',
    'stickyuploads',
    'messaging',
    'geoposition',
    'haystack',
    'widget_tweaks',
    #    'social.apps.django_app.default',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'cleff.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'social.apps.django_app.context_processors.backends',
                # 'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'cleff.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cleff',  # 'db_name',
        'USER': 'cleff',  # 'db_user',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,
                          "static/media")  # /Users/lancerogers/Developer/music-network/music-network/cleff/static/media"
MEDIA_URL = '/media/'



STATIC_ROOT = os.path.join(BASE_DIR, '/static/')
#STATIC_URL = '/static/'


#EDIA_ROOT = os.path.join(BASE_DIR,
  #                        "static/media")  # /Users/lancerogers/Developer/music-network/music-network/cleff/static/media"
#MEDIA_URL = '/media/'


# AUTHENTICATION_BACKENDS = (
#   'social.backends.facebook.FacebookOAuth2',
#  'social.backends.google.GoogleOAuth2',
# 'social.backends.twitter.TwitterOAuth',
#  'django.contrib.auth.backends.ModelBackend',
# )


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',

)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
     #   'URL': 'http://192.168.1.82:9200/',
        'INDEX_NAME': 'haystack',
        'INCLUDE_SPELLING': 'False',
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


'''
GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'maxZoom': 8,
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}
'''
