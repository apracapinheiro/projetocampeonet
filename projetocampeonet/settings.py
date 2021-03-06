# -*- coding: utf-8 -*-
"""
Django settings for projetocampeonet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOCAL = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9kjy7(jv@r@g+e_j3u%axctqc$kcib6(t#^giycn)_+c#a*435'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cadastros',
    'palpites',
    'debug_toolbar',
    'bootstrap3'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'projetocampeonet.urls'

WSGI_APPLICATION = 'projetocampeonet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Araguaina'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/fotos/' #"apelido" do caminho das imagens

STATIC_ROOT = os.path.join(LOCAL, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'static') #caminho fisico onde se encontra os arquivos de imagens

STATICFILES_DIRS = (
   BASE_DIR + '/static/',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

# email config para teste do password_reset em modo DEBUG

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = '127.0.0.1'
# EMAIL_PORT = 1025
# EMAIL_USE_TLS = False
# DEFAULT_FROM_EMAIL = 'testing@example.com'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'falcaof1@gmail.com'
EMAIL_HOST_PASSWORD = 'juoukdittrqillwa'
EMAIL_PORT = 587
EMAIL_USE_TLS = True