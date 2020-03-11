
import os

from StoreAPI.settings import BASE_DIR

# DEBUG = True
# THUMBNAIL_DEBUG = True

PUBLIC_FILES_DIR = os.path.dirname(__file__)

STATIC_ROOT = os.path.join(PUBLIC_FILES_DIR, 'static-collection')
MEDIA_ROOT = os.path.join(PUBLIC_FILES_DIR, 'media')
STATICFILES_DIRS = [os.path.join(PUBLIC_FILES_DIR, 'static')]

