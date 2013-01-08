import os
import sys

sys.path.append('/home/jackpoint/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'jackpoint.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()