import os

DJANGO_PROJECT_ROOT = os.path.abspath('%s/../' % os.path.dirname(__file__))

INTERNAL_IPS = ('127.0.0.1',)

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '%s/et_issue_example/db.sqlite3' % DJANGO_PROJECT_ROOT
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(DJANGO_PROJECT_ROOT, 'collected_static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a2#gn&(!hypas+6-$epnti$ix#5n9*6d=no2wx&zxgjy-oda93'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'et_issue_example.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'et_issue_example.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'debug_toolbar',
    'easy_thumbnails',
    'storages',
    'photos',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# DJANGO DEBUG TOOLBAR
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# EASY THUMBNAIL SETTINGS
THUMBNAIL_ALIASES = {
    '': {
        'admin_thumbnail': {'size': (120, 80), 'crop': 'scale', 'quality': 80},
        'admin_thumbnail_small': {'size': (50, 50), 'crop': 'scale', 'quality': 80},
        'admin_thumbnail_cropped': {'size': (120, 120), 'crop': 'crop', 'quality': 80},
        'profile_photo_thumbnail': {'size': (170, 170), 'crop': 'crop', 'quality': 80},
        'event_thumbnail': {'size': (160, 120), 'crop': 'crop', 'quality': 90},
        'article_photo_thumbnail': {'size': (210, 280), 'quality': 80},
        'photoset_large': {'size': (555, 370), 'quality': 80},
        'photoset_small': {'size': (58, 40), 'crop': 'crop', 'quality': 80},
        'large_photo': {'size': (960, 720), 'quality': 80},
    },
}

# PIL FIX
from PIL import ImageFile
# The following fixes the PIL "Suspension not allowed here" error
# 1048576 Bytes = 1M
ImageFile.MAXBLOCK = 1048576

# AWS SETTINGS
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
STATIC_URL = 'http://%s.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = 'http://%s.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE = 'et_issue_example.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'et_issue_example.s3utils.StaticRootS3BotoStorage'
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
AWS_S3_SECURE_URLS = True
AWS_QUERYSTRING_AUTH = False
