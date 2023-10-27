import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = '*+uiasgfhfhea(0_=n@c6aacvxcd*xtaassdkjlgvzo'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'istudent_db',
        'USER': 'medet',
        'PASSWORD': 'diplom2023',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
CSRF_TRUSTED_ORIGINS = ['http://istudent.kz', 'http://195.210.47.115']
