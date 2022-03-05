"""
WSGI config for runder_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# assuming your Django settings file is at
path = '/Users/yukikondo/Django/runder/runder_project/runder_project/settings.py'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'runder_project.settings')

application = get_wsgi_application()

