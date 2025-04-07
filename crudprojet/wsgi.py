"""
WSGI config for crudprojet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudprojet.settings')
django.setup()

# Exécuter les migrations à chaque démarrage
from django.core.management import call_command
call_command('migrate')

application = get_wsgi_application()
