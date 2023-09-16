from pathlib import Path
import os
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = 'django-insecure-m((_87@c6z2ja$tut2s^y##=3@i0c3ovl)4ay$s9%b+$*5l81g'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',  # Third party
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',    # Third party
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Local
    'apps.api',
    'apps.clients',
    'apps.tours',
    'apps.videos',

    # Third party
    'django_cleanup.apps.CleanupConfig',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

# Third party
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5500',
]
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://127.0.0.1:5500',
]
CORS_ORIGIN_ALLOW_ALL = True

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=36500),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=73000),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # Third party
    'corsheaders.middleware.CorsMiddleware',    # Third party
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

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

WSGI_APPLICATION = 'src.wsgi.application'

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

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage'
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1