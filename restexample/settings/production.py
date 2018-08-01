from .base import *

# ##### ENVIRONMENT VARIABLES & SECURITY CONFIGURATION ####

DEBUG = False

ALLOWED_HOSTS = ['api.laziness.xyz']

# ##### DATABASE CONFIGURATION #########################

# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS += [
]
