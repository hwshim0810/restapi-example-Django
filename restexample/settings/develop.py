import os
from .base import *

# ##### ENVIRONMENT VARIABLES & SECURITY CONFIGURATION ####

DEBUG = True


# ##### DATABASE CONFIGURATION #########################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(ROOT_DIR, 'db.sqlite3'),
    }
}

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS += [

    # django-debug-toolbar
    "debug_toolbar",

    # django-extensions
    'django_extensions',

]

# ## DEBUG TOOLBAR

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}
