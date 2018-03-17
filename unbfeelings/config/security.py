"""
secret key to the project.

https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
"""

import os

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    '8qvyp%u9wnd7t(lkjair+#lbx)qr8=jsu#o5uk4+c=xru&ujl+'
)
