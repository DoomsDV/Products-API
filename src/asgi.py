"""
ASGI config for src project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from dotenv import load_dotenv
from django.core.asgi import get_asgi_application

load_dotenv()
if os.environ.get('DJANGO_ENV') == 'development':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
elif os.environ.get('DJANGO_ENV') == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.productions')

application = get_asgi_application()
