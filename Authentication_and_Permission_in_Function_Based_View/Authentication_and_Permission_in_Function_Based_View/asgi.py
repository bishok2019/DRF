"""
ASGI config for Authentication_and_Permission_in_Function_Based_View project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Authentication_and_Permission_in_Function_Based_View.settings')

application = get_asgi_application()
