"""
File responsible for inserting applications within the project.
"""

APPS_DJANGO = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

EXTERNAL_APPS = [
    'rest_framework',
    'corsheaders',
    'rest_framework_swagger',
]

LOCAL_APPS = ['api']

PRODUCTION_APPS = APPS_DJANGO + EXTERNAL_APPS + LOCAL_APPS

DEVELOPMENT_APPS = ['django_extensions'] + PRODUCTION_APPS
