"""
WSGI config for dongtaoy_oa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
path = "/home/dongtaoy/Dropbox/Projects/dongtaoy_oa/"
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dongtaoy_oa.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
