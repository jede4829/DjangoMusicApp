
from pathlib import Path
import os
import dj_database_url ## Heroku
import dotenv ## Heroku
import django_heroku ## Heroku

BASE_DIR_ONE = Path(__file__).resolve().parent.parent ## Ignored - Heroku - Breaks CSS - DM - DM2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = 'htvgqqdfq8e(abu*yj5y5)aa@+n=6^g&sj135nokg!20sl$jwy'
DEBUG = True
ALLOWED_HOSTS = [
    '0.0.0.0', ## Heroku
    'jamjelly.herokuapp.com', ## Heroku
    '127.0.0.1' ## Heroku
]

INSTALLED_APPS = [
    'search.apps.searchConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware', ## Heroku
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'musicsite.urls'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' ## Heroku

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
            ],
        },
    },
]

WSGI_APPLICATION = 'musicsite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR_ONE / 'db.sqlite3', # - DM2
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__)) ## Heroku - Breaks CSS
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'), ## RM Heroku - DM
	# os.path.join(PROJECT_ROOT,'static'), ## Heroku - Breaks CSS - DM
]

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles') ## Heroku - Medium - DM
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # - DM
