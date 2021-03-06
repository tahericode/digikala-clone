"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 2.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# os
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x8m1^mf3+@*o3#0yt_r*a5ekeq$9!wx1)$(oj3(9y4tkk=pmu7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    # Third Parties
    'ckeditor',
    'ckeditor_uploader',
    'taggit',
    'crispy_forms',
    'phonenumber_field',
    'jalali_date',
    'rosetta',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', 
    'translated_fields',
    # Apps
    'shop',
    'details',
    'cart',
    'orders',
    'blog',
    'account',
    'payment',
    'coupons',
    'message',
]


# Default for jalali_date

JALALI_DATE_DEFAULTS = {
    'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            'admin/js/django_jalali.min.js',
            # or
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}




# SITE ID
SITE_ID = 1

# FOR CK_EDITOR 
CKEDITOR_UPLOAD_PATH = 'ck-uploads/'
CKEDITOR_ALLOW_NONIMAGE_FILES = False

# FOR CRISPY 
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',   #middleware for Bilingual
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

# FOR TEMPLATES
TEMPLATES = [
    {
        # FOR BACKEND(backend.py)
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # To identify templates
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                # for context_processors
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                # context_processors for blog
                'blog.context_processors.blogSidebarInfo',
                # context_processing for public messages
                'message.context_processors.publicMesseges'
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/


# import gettext_lazy 
from django.utils.translation import gettext_lazy as _


# languge for Bilingual
LANGUAGES = (
    ('en',_('English')),
    ('fa', _('Persion')),
)


# language code 
LANGUAGE_CODE = 'fa-ir'




# locale paths in rootdirectory
LOCALE_PATHS = (
    os.path.join(BASE_DIR,'locale/'),
)

# to timezone(date)
TIME_ZONE = 'Asia/Tehran'
# for translate
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# Crispy
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Login & Logout
LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = '/'

# Statics
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')
CKEDITOR_UPLOAD_PATH = "uploads/"

# Cart session id 
CART_SESSION_ID = 'cart'



#login with email and username
AUTHENTICATION_BACKENDS = ('account.backend.EmailorUsernameModelBackend',)

# REDIS
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1