"""
Django settings for sphynx project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ky5jos-2*0boo_&yo26ibd4x&6dw-8*^6)^9h!ri5^il&(g-q_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taws',
    'GitApp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'KATE.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'KATE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'KATE' ,
	'USER': 'smosql' ,
	'PASSWORD' : 'sm@ptics' ,
	'PORT': '3306' ,
	'HOST': '151.98.52.73'
    }
}


# JENKINS ENVIRONMENT VARIABLES

JENKINS = {
    'HOST': 'http://151.98.52.72:7001',
    'SUITEFOLDER': '/tools/jksadmin/SERVER_POOL/JEN001/jobs/',
    'JOB_STRUCT': '/workspace/'
}


# TEMPLATE FILES
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEST_TEMPLATE = TEMPLATES_DIR + '/taws/testTemplate.txt'
JOB_PROPS_TEMPLATE = TEMPLATES_DIR + '/taws/tempProperties.xml'
JOB_TEMPLATE = TEMPLATES_DIR + '/taws/tempJenkins.xml'


GIT_REPO = '/GITREPOS/KATETESTS'
TAG_SPLIT = '@'
TPS_SPLIT = '__'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/'

STATIC_ROOT = '/var/www/static/'

STATICFILES_DIRS = (
    ("assets",BASE_DIR + "/static"),
    os.path.join('static'),
)



#SESSION SETTINGS

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 3600
SESSION_SAVE_EVERY_REQUEST = True

#LDAP CONFIGURATION

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, PosixGroupType


# Baseline configuration.

AUTH_LDAP_SERVER_URI = "ldap://151.98.52.70"
AUTH_LDAP_BIND_DN = "uid=smotools,ou=Application Users,dc=it.alcatel-lucent,dc=com"
AUTH_LDAP_BIND_PASSWORD = "smo@2015"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=Users,dc=it.alcatel-lucent,dc=com",
    ldap.SCOPE_SUBTREE, "(cn=%(user)s)")
# or perhaps:
# AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=Users,dc=maxcrc,dc=com"

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Groups,dc=it.alcatel-lucent,dc=com",
    ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)"
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType()

# Simple group restrictions
AUTH_LDAP_REQUIRE_GROUP = "cn=Automation,ou=Groups,dc=it.alcatel-lucent,dc=com"

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "cn",
    "last_name": "sn",
    "email": "mail"
}

#AUTH_LDAP_PROFILE_ATTR_MAP = {
#    "employee_number": "employeeNumber"
#}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=Automation,ou=Groups,dc=it.alcatel-lucent,dc=com",
    "is_staff": "cn=Users,ou=Groups,dc=it.alcatel-lucent,dc=com",
    "is_superuser": "cn=Automation,ou=Groups,dc=it.alcatel-lucent,dc=com"
}

#AUTH_LDAP_PROFILE_FLAGS_BY_GROUP = {
#    "is_awesome": "cn=awesome,ou=django,ou=groups,dc=example,dc=com",
#}

# Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache group memberships for an hour to minimize LDAP traffic
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600


# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
 


#import logging

#logger = logging.getLogger('django_auth_ldap')
#logger.addHandler(logging.StreamHandler())
#logger.setLevel(logging.DEBUG)                                      
