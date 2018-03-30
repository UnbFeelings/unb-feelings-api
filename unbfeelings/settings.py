"""
Django settings for unbfeelings project.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

# Not remove the imports.
from unbfeelings.config.apps import (
    PRODUCTION_APPS, DEVELOPMENT_APPS
)
from unbfeelings.config.database import (
    DEVELOPMENT_DB, PRODUCTION_DB
)
from unbfeelings.config.files import (
    STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL
)
from unbfeelings.config.i18n import (
    LANGUAGE_CODE, TIME_ZONE, USE_I18N, USE_L10N, USE_TZ
)
from unbfeelings.config.rest import (
    REST_FRAMEWORK, JWT_AUTH
)
from unbfeelings.config.authentication import (
    AUTHENTICATION_BACKENDS, AUTH_USER_MODEL
)
from unbfeelings.config.middleware import MIDDLEWARE
from unbfeelings.config.security import SECRET_KEY
from unbfeelings.config.templates import TEMPLATES
from unbfeelings.config.password import AUTH_PASSWORD_VALIDATORS
import os

MODE_ENVIROMENT = os.getenv("MODE_ENVIROMENT", "development")

ROOT_URLCONF = 'unbfeelings.urls'
WSGI_APPLICATION = 'unbfeelings.wsgi.application'
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']

if MODE_ENVIROMENT == 'development':
    DEBUG = True
    DATABASES = DEVELOPMENT_DB
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    INSTALLED_APPS = DEVELOPMENT_APPS

elif MODE_ENVIROMENT == 'production':
    DEBUG = False
    DATABASES = PRODUCTION_DB
    INSTALLED_APPS = PRODUCTION_APPS
