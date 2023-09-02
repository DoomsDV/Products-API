"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv()
if os.environ.get('DJANGO_ENV') == 'development':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
elif os.environ.get('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.productions')

application = get_wsgi_application()
