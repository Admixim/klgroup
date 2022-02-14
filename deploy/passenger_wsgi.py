import os, sys
sys.path.insert(0, '/var/www/u1344452/data/www/klgroup24.ru/crm')
sys.path.insert(1, '/var/www/u1344452/data/www/env_crm/lib/python3.8/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'crm.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()