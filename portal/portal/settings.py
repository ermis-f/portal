"""
Django settings for portal project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import ldap
from django_auth_ldap.config import LDAPSearch,GroupOfNamesType, PosixGroupType,NestedGroupOfNamesType
from django.conf import settings

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
    #'guardian.backends.ObjectPermissionBackend'
    #    'django_auth_ldap.backend.LDAPBackend',
    #'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = 'ldap://ermis-floods.aegean.gr'
LDAP_SEARCH_DN = 'cn=users,dc=ermis-floods,dc=aegean,dc=gr'
AUTH_LDAP_USER = '(uid=%(user)s)'
AUTH_LDAP_BIND_DN = 'cn=admin,dc=ermis-floods,dc=aegean,dc=gr'
AUTH_LDAP_BIND_PASSWORD = 'Erm_F2018_Lusers'


AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName','last_name':'sn','email':'Email'
}
AUTH_LDAP_USER_SEARCH = LDAPSearch(LDAP_SEARCH_DN,
                                   ldap.SCOPE_SUBTREE, AUTH_LDAP_USER)

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    'ou=geonode,dc=ermis-floods,dc=aegean,dc=gr',
    ldap.SCOPE_SUBTREE,
    '(objectClass=groupOfNames)',
)
AUTH_LDAP_GROUP_TYPE =  NestedGroupOfNamesType()
#AUTH_LDAP_REQUIRE_GROUP = "ou=geonode,dc=ermis-floods-dev,dc=aegean,dc=gr"

AUTH_LDAP_FIND_GROUP_PERMS=True
AUTH_LDAP_MIRROR_GROUPS=True
AUTH_LDAP_ALWAYS_UPDATE_USER=True
AUTH_LDAP_AUTHORIZE_ALL_USERS=True

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=active,ou=geonode,dc=ermis-floods,dc=aegean,dc=gr",
    "is_staff": "cn=staff,ou=geonode,dc=ermis-floods,dc=aegean,dc=gr",
    "is_superuser": "cn=superuser,ou=geonode,dc=ermis-floods,dc=aegean,dc=gr",
    "aeguni": "cn=aeguni,ou=geonode,dc=ermis-floods,dc=aegean,dc=gr",
    "creteuni": "cn=creteuni,ou=geonode,dc=ermis-floods,dc=aegean,dc=gr",
    "cyprusinst": "cn=cyprusinst,ou=geonode,dc=ermis-floods,dc=aegean,dc=gr",
}

#AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CONNECTION_OPTIONS = {
ldap.OPT_DEBUG_LEVEL: 3,
ldap.OPT_REFERRALS: 0,
}
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*!5l+$(j8++he77zx66&4h3lp2r!&a+^h$#3&uy37fag4dz0$g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['195.251.137.46','localhost','ermis-floods-dev.aegean.gr']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'dl_user',
    'anymail',
    'crispy_forms',
    'bootstrap3',
    'mama_cas',
    'portal',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':   [ os.path.join(BASE_DIR, 'templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS=['/home/geo/Envs/rEnv/portal/static/',]
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static/'),
]
#STATIC_ROOT= os.path.join(BASE_DIR, 'static/')
#STATIC_ROOT = "/home/geo/Envs/rEnv/portal/static/"

#ldap registration settings
# Site
SITE_BASE_URL = 'http://ermis-floods-dev.aegean.gr' # No trailing slash

#TIME_ZONE = 'Africa/Nairobi'

# IDP Details
IDP_NAME = 'ERMIS FLOODS DEVELOPMENT SERVER'
IDP_LOGO = 'https://ermis-f.eu/wp-content/uploads/2018/06/Ermisxlnew2-672x368.png' # Width of 200px at least

# Test service provider
#SERVICE_PROVIDER = 'Test service provider'
#SERVICE_PROVIDER_URL = 'https://test-service.kenet.or.ke'

# This setting enables capturing of a users institution and country details
IDP_CATCH_ALL = False

# LDAP Settings

LDAP_PROTO = 'ldap'
LDAP_HOST = 'ermis-floods.aegean.gr'
LDAP_PORT = '389' # must be str
LDAP_BASE_DN = 'cn=users,dc=ermis-floods,dc=aegean,dc=gr'
LDAP_BIND_DN = 'cn=admin,dc=ermis-floods,dc=aegean,dc=gr'
LDAP_BIND_DN_CREDENTIAL = 'Erm_F2018_Lusers'
LDAP_GID = "501" # group ID to add signed up users
LDAP_BASE_UID = 1000 # Integer

# Password Reset

PASSWORD_RESET_TOKEN_EXPIRY = 1 #Hours

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.aegean.gr'
EMAIL_PORT = '587'
#EMAIL_HOST_USER = 'aegean\guestgeo'
#EMAIL_HOST_PASSWORD = 'Pass_Temp!'
EMAIL_HOST_USER = 'vkopsachilis'
EMAIL_HOST_PASSWORD = 'geo-812!'
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 100

DEFAULT_FROM_EMAIL = IDP_NAME + ' <vkopsachilis@geo.aegean.gr>'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
LDAP_USER_DATA = ['sn', 'uid',  ]

TESTING = True
RECAPTCHA_PUBLIC_KEY ='6LeBoKEUAAAAAM6lLPhO_vngqMxZXah8yYEhl5jo'  #'6LcYz5sUAAAAALugnwO42-eviOOdDoEjC5E4SjPP'
RECAPTCHA_PRIVATE_KEY = '6LeBoKEUAAAAAIReGZno11LiqESCMQkRlOCfxRqC' #'6LcYz5sUAAAAACLB0LbxVzdNTqtdwvw2Zn0by6ma'
BOOTSTRAP3 = { "theme_url": "https://bootswatch.com/3/flatly/bootstrap.min.css",   }