
from pathlib import Path
import os
import dj_database_url
import dotenv
import django_heroku


BASE_DIR = Path(__file__).resolve().parent.parent
#NEW FOR HEROKU
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
	dotenv.load_dotenv(dotenv_file)


SECRET_KEY = 'htvgqqdfq8e(abu*yj5y5)aa@+n=6^g&sj135nokg!20sl$jwy'
DEBUG = True
ALLOWED_HOSTS = [
    '0.0.0.0',
    'mysterious-cliffs-00315.herokuapp.com',
    '127.0.0.1'
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
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'musicsite.urls'

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

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

#NEW FOR HEROKU
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)


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
STATIC_URL = '/static/'

# ---------- When running locally use this ----------

#STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

# ---------- When running remotely uncommet below, comment the above ----------

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR,'static')

# This should already be in your settings.py
django_heroku.settings(locals())
# This is new
options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)
