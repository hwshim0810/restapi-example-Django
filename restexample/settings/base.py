import os
import sys
import environ

# ##### ENVIRONMENT VARIABLES & SECURITY CONFIGURATION ####

env = environ.Env()

SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# ##### PATH CONFIGURATION ################################

# Project root
ROOT_DIR = environ.Path(__file__) - 3

# Apps root
APPS_DIR = ROOT_DIR.path('apps')

# Collecting root
COLLECT_ROOT = ROOT_DIR.path('dist')

# Static root
STATIC_ROOT = COLLECT_ROOT.path('static')

# Media root
MEDIA_ROOT = COLLECT_ROOT.path('media')

# Append app dir
sys.path.append(os.path.normpath(APPS_DIR))

# ##### STATIC CONFIGURATION ################################

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]


# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = [

    # ## Django apps ##
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # ## Project apps ##
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'restexample.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates'))
        ],
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

# ##### DJANGO RUNNING CONFIGURATION ######################

ADMIN_URL = env('DJANGO_ADMIN_URL', default=r'^admin/')

WSGI_APPLICATION = 'restexample.wsgi.application'

SITE_ID = 1

# ##### AUTHENTICATION CONFIGURATION ######################

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# ##### INTERNATIONALIZATION CONFIGURATION ################

# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# ##### EMAIL CONFIGURATION ######################

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
