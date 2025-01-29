"""
WSGI config for low_level_program project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import atexit

from low_level_program.startup import main_close

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'low_level_program.settings')

application = get_wsgi_application()

atexit.register(main_close)
