from .base import *

ALLOWED_HOSTS = ['192.168.56.103'] # 서버의 고정 IP
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False