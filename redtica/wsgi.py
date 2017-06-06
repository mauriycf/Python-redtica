import os
import sys
import site
from django.core.wsgi import get_wsgi_application

path = '/var/www/proyecto'

if path not in sys.path:
    sys.path.append(path)

vepath = path +'/venv/lib/python3.4/site-packages'

prev_sys_path = list(sys.path)
# add the site-packages of our virtualenv as a site dir
site.addsitedir(vepath)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redtica.settings")
application = get_wsgi_application()
