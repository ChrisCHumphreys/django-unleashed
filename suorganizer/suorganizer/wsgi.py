"""
WSGI config for suorganizer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.cache.backends.memcached import \
	BaseMemcachedCache
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "suorganizer.settings")

BaseMemcachedCache.close = lambda self, **kwargs: None

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

"""
old Code

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "suorganizer.settings")

application = get_wsgi_application()
"""
