"""
Django settings for DEP project.

Generated by 'django-admin startproject' using Django 2.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Path to mdmctl bash script.
RUN_AS_youraccount = os.path.join(BASE_DIR, 'run_as_youraccount.sh')

if not os.path.exists(RUN_AS_youraccount):
    sys.exit("{} doesn't exist.".format(RUN_AS_youraccount))

################################################################################
# Path to API bash script.
SYNC_DEP_DEVICES = os.path.join(BASE_DIR, 'scripts/sync_dep_devices.sh')


if not os.path.exists(SYNC_DEP_DEVICES):
    sys.exit("{} doesn't exist.".format(SYNC_DEP_DEVICES)) 
################################################################################
################################################################################
# Path to API bash script.
SYNC_FLEET_DEVICES = os.path.join(BASE_DIR, 'scripts/sync_fleet_devices.sh')


if not os.path.exists(SYNC_FLEET_DEVICES):
    sys.exit("{} doesn't exist.".format(SYNC_FLEET_DEVICES)) 
################################################################################

################################################################################
# Path to GenCSR bash script.
GENERATE_CSR = os.path.join(BASE_DIR, 'scripts/generate_csr.sh')


if not os.path.exists(GENERATE_CSR):
    sys.exit("{} doesn't exist.".format(GENERATE_CSR)) 
################################################################################

RESTART_DEVICE = os.path.join(BASE_DIR, 'scripts/restart_device_uniq.sh')

if not os.path.exists(RESTART_DEVICE):
    sys.exit("{} doesn't exist.".format(RESTART_DEVICE)) 
################################################################################

ERASE_DEVICE = os.path.join(BASE_DIR, 'scripts/erase_device_uniq.sh')

if not os.path.exists(ERASE_DEVICE):
    sys.exit("{} doesn't exist.".format(ERASE_DEVICE))
################################################################################

LOCK_DEVICE = os.path.join(BASE_DIR, 'scripts/lock_device_uniq.sh')

if not os.path.exists(LOCK_DEVICE):
    sys.exit("{} doesn't exist.".format(LOCK_DEVICE))
################################################################################
################################################################################

PUSH_NOTIFICATION = os.path.join(BASE_DIR, 'scripts/push_notification_uniq.sh')

if not os.path.exists(PUSH_NOTIFICATION):
    sys.exit("{} doesn't exist.".format(PUSH_NOTIFICATION))
################################################################################
################################################################################

SSO_EU = os.path.join(BASE_DIR, 'scripts/sso_eu.sh')

if not os.path.exists(SSO_EU):
    sys.exit("{} doesn't exist.".format(SSO_EU))
################################################################################
################################################################################

SSO_JP = os.path.join(BASE_DIR, 'scripts/sso_jp.sh')

if not os.path.exists(SSO_JP):
    sys.exit("{} doesn't exist.".format(SSO_JP))
################################################################################
################################################################################

SSO_TW = os.path.join(BASE_DIR, 'scripts/sso_tw.sh')

if not os.path.exists(SSO_TW):
    sys.exit("{} doesn't exist.".format(SSO_TW))
################################################################################
################################################################################

SSO_US = os.path.join(BASE_DIR, 'scripts/sso_us.sh')

if not os.path.exists(SSO_US):
    sys.exit("{} doesn't exist.".format(SSO_US))
################################################################################
################################################################################

SSO_PH = os.path.join(BASE_DIR, 'scripts/sso_ph.sh')

if not os.path.exists(SSO_PH):
    sys.exit("{} doesn't exist.".format(SSO_PH))
################################################################################
################################################################################

TCC_ZOOM = os.path.join(BASE_DIR, 'scripts/tcc_zoom.sh')

if not os.path.exists(TCC_ZOOM):
    sys.exit("{} doesn't exist.".format(TCC_ZOOM))
################################################################################


PUSH_APP = os.path.join(BASE_DIR, 'scripts/push_app_uniq.sh')

if not os.path.exists(PUSH_APP):
    sys.exit("{} doesn't exist.".format(PUSH_APP)) 
################################################################################

REMOVE_APP = os.path.join(BASE_DIR, 'scripts/remove_app_uniq.sh')

if not os.path.exists(REMOVE_APP):
    sys.exit("{} doesn't exist.".format(REMOVE_APP))
################################################################################
################################################################################

REMOVE_TCC_ZOOM = os.path.join(BASE_DIR, 'scripts/remove_tcc_zoom.sh')

if not os.path.exists(REMOVE_TCC_ZOOM):
    sys.exit("{} doesn't exist.".format(REMOVE_TCC_ZOOM))
################################################################################

PUSH_UPDATE = os.path.join(BASE_DIR, 'scripts/push_update_uniq.sh')

if not os.path.exists(PUSH_UPDATE):
    sys.exit("{} doesn't exist.".format(PUSH_UPDATE))

################################################################################
DOWNLOADONLY_UPDATE = os.path.join(BASE_DIR, 'scripts/push_update_downloadonly.sh')

if not os.path.exists(DOWNLOADONLY_UPDATE):
    sys.exit("{} doesn't exist.".format(DOWNLOADONLY_UPDATE))

################################################################################
DEFAULT = os.path.join(BASE_DIR, 'scripts/push_update_default.sh')

if not os.path.exists(DEFAULT):
    sys.exit("{} doesn't exist.".format(DEFAULT))

################################################################################

INSTALL_PROFILE = os.path.join(BASE_DIR, 'scripts/install_profile_uniq.sh')

if not os.path.exists(INSTALL_PROFILE):
    sys.exit("{} doesn't exist.".format(INSTALL_PROFILE))

################################################################################

UPDATE_ENROLL_PROFILE = os.path.join(BASE_DIR, 'scripts/update_enroll_profile_uniq.sh')

if not os.path.exists(UPDATE_ENROLL_PROFILE):
    sys.exit("{} doesn't exist.".format(UPDATE_ENROLL_PROFILE))

################################################################################
REMOVE_PROFILE = os.path.join(BASE_DIR, 'scripts/remove_profile_uniq.sh')

if not os.path.exists(REMOVE_PROFILE):
    sys.exit("{} doesn't exist.".format(REMOVE_PROFILE))
# Path to mobileconfig
################################################################################
MOBILECONF = os.path.join(BASE_DIR, 'profiles/test.mobileconfig')

if not os.path.exists(MOBILECONF):
    sys.exit("{} doesn't exist.".format(MOBILECONF))

################################################################################

# Path to mdmctl .json.
#ServerSide
#MDMCTL_JSON = os.path.join('/home/youraccount/DEP-Config/DEP-Profile.json')
MDMCTL_JSON = os.path.join(BASE_DIR, 'configs/DEP-Profile.json')
#MDMCTL_JSON = os.path.join('/home/youraccount/DEP-Config/DEP-Profile.json')
if not os.path.exists(MDMCTL_JSON):
    sys.exit("{} doesn't exist.".format(MDMCTL_JSON))

EU_JSON = os.path.join(BASE_DIR, 'configs/EU.json')
if not os.path.exists(EU_JSON):
    sys.exit("{} doesn't exist.".format(EU_JSON))

TW_JSON = os.path.join(BASE_DIR, 'configs/TW.json')
if not os.path.exists(TW_JSON):
    sys.exit("{} doesn't exist.".format(TW_JSON))

JP_JSON = os.path.join(BASE_DIR, 'configs/JP.json')
if not os.path.exists(JP_JSON):
    sys.exit("{} doesn't exist.".format(JP_JSON))

PH_JSON = os.path.join(BASE_DIR, 'configs/PH.json')
if not os.path.exists(PH_JSON):
    sys.exit("{} doesn't exist.".format(PH_JSON))

US_JSON = os.path.join(BASE_DIR, 'configs/US.json')
if not os.path.exists(US_JSON):
    sys.exit("{} doesn't exist.".format(US_JSON))

AU_JSON = os.path.join(BASE_DIR, 'configs/AU.json')
if not os.path.exists(AU_JSON):
    sys.exit("{} doesn't exist.".format(AU_JSON))

SG_JSON = os.path.join(BASE_DIR, 'configs/SG.json')
if not os.path.exists(SG_JSON):
    sys.exit("{} doesn't exist.".format(SG_JSON))

IOS_JSON = os.path.join(BASE_DIR, 'configs/iOS.json')
if not os.path.exists(IOS_JSON):
    sys.exit("{} doesn't exist.".format(IOS_JSON))

EU_TXT = os.path.join(BASE_DIR, 'configs/eu.txt')
if not os.path.exists(EU_TXT):
    sys.exit("{} doesn't exist.".format(EU_TXT))

HTTP_POST_DATA = os.path.join(BASE_DIR, 'configs/HTTP_POST_DATA.json')

if not os.path.exists(HTTP_POST_DATA):
    sys.exit("{} doesn't exist.".format(HTTP_POST_DATA))


TRAFIC_DATA = os.path.join(BASE_DIR, 'configs/TRAFIC_DATA.json')
#TRAFIC_DATA = os.path.join(BASE_DIR, '/var/json/TRAFIC_DATA.json')

if not os.path.exists(TRAFIC_DATA):
    sys.exit("{} doesn't exist.".format(TRAFIC_DATA))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xujs+pit_xa6roomp#m2=%y#*u48gi^)ag$p$@^0%8swc=%d5t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

#ServerSide
#DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'DEP',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'DEP.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'DEP.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, "configs/database.sqllite3"), #ServerSide '/var/db/dep_tool/database.sqllite3'
        #'NAME': '/var/db/deptool/database.sqllite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')

MEDIA_URL = '/upload/'


# SENDFILE settings
SENDFILE_BACKEND = 'sendfile.backends.development'
#SENDFILE_BACKEND = 'sendfile.backends.xsendfile'
#SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_ROOT = os.path.join(BASE_DIR, 'upload/')
SENDFILE_URL = '/upload/'