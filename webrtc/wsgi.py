"""
WSGI config for webrtc project.

It exposes the WSGI callable as a module-level variable named ``application``.


"""

import os

from django.core.wsgi import get_wsgi_application
from importlib import import_module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webrtc.settings")

application = get_wsgi_application()