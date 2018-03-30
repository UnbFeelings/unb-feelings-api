"""
File responsible for the project authentication.
"""

AUTHENTICATION_BACKENDS = [
    'api.backends.EmailBackend'
]

AUTH_USER_MODEL = 'api.Student'
