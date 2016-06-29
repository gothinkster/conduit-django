import dj_database_url
from conduit.settings.common import *

SECRET_KEY =  os.environ.get('SECRET_KEY')

DEBUG = False

DATABASES = {
  'default': dj_database_url.config()
}
