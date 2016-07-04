from app.settings import *
import dj_database_url

#settings for production 
ALLOWWED_HOSTS =['zigmu.herokuapp.com']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')

DEBUG = False
TEMPLATE_DEBUG = True
#for database
DATABASES['default'] = dj_database_url.config()
# for serving satic files in a production server
STATICFILES_DIRS = ( os.path.join(BASE_DIR,'static'), )
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
#added
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


