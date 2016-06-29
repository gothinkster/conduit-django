from conduit.settings.common import *

SECRET_KEY = '13q$v6_po-j^dxlt2b!w(!5j0mf**w8g$&%z0205o7ephoph(p'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
