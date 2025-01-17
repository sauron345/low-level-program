"""
WSGI config for recruitment_task_krypton project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import atexit

from recruitment_task_krypton.startup import close_gateways

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recruitment_task_krypton.settings')

application = get_wsgi_application()

atexit.register(close_gateways)
