import sys
from django.utils.translation import ugettext_lazy as _
from hamlpy import templatize

# Django settings for tns_glass project.
THUMBNAIL_DEBUG = False

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Nyaruka', 'code@nyaruka.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'tracpro.sqlite',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# set the mail settings, we send throught gmail
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'server@nyaruka.com'
DEFAULT_FROM_EMAIL = 'server@nyaruka.com'
EMAIL_HOST_PASSWORD = 'NOTREAL'
EMAIL_USE_TLS = True

API_ENDPOINT = 'http://localhost:8001'
SITE_HOST_PATTERN = 'http://%s.localhost:8000'
SITE_CHOOSER_TEMPLATE = 'public/org_chooser.haml'

# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone
TIME_ZONE = 'GMT'
USER_TIME_ZONE = 'GMT'
USE_TZ = True

MODELTRANSLATION_TRANSLATION_REGISTRY = "translation"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

# Available languages for translation
LANGUAGES = (('en', _("English")), ('fr', _("French")), ('ps', _("Pashto")), ('fa', _("Persian")))
RTL_LANGUAGES = set(['ps', 'fa'])
DEFAULT_LANGUAGE = "en"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/sitestatic/'
COMPRESS_URL = '/sitestatic/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/sitestatic/admin/'

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
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'Q#9JgQuBlOvUt#Y*LuduDO6L#JrWQ%hRT3*6ALdcPHNQWLqXaiMHy6jSC6$&Chx2Zab38wO&tBg@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'hamlpy.template.loaders.HamlPyFilesystemLoader',
    'hamlpy.template.loaders.HamlPyAppDirectoriesLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    
#     'django.template.loaders.eggs.Loader',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',    
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'dash.orgs.context_processors.user_group_perms_processor',
    'dash.orgs.context_processors.set_org_processor',
    'dash.context_processors.lang_direction'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'dash.orgs.middleware.SetOrgMiddleware',
)

ROOT_URLCONF = 'tracpro.urls'

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:1',
        'OPTIONS': {
            'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
        }
    }
}

if 'test' in sys.argv:
    CACHES['default'] = {'BACKEND': 'django.core.cache.backends.dummy.DummyCache',}


ORG_CONFIG_FIELDS =[dict(name='chat_api_token', field=dict(help_text=_("The API token for the chat organization for this org"),
                         required=True))]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # mo-betta permission management
    'guardian',

    # error logging
    'raven.contrib.django',

    # versioning of our data
    'reversion',

    # the django admin
    'django.contrib.admin',

    # compress our CSS and js
    'compressor',

    # thumbnail
    'sorl.thumbnail',

    # smartmin
    'smartmin',

    # import tasks
    'smartmin.csv_imports',

    # users
    'smartmin.users',

    # async tasks,
    'djcelery',

    # dash apps
    'dash.orgs',
    'dash.dashblocks',
    'dash.stories',
    'dash.utils',
    'dash.categories',

    # supervisors
    'tracpro.supervisors',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'httprouterthread': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

#-----------------------------------------------------------------------------------
# Directory Configuration
#-----------------------------------------------------------------------------------
import os

PROJECT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))
RESOURCES_DIR = os.path.join(PROJECT_DIR, '../resources')

LOCALE_PATHS = (os.path.join(PROJECT_DIR, '../locale'),)
RESOURCES_DIR = os.path.join(PROJECT_DIR, '../resources')
FIXTURE_DIRS = (os.path.join(PROJECT_DIR, '../fixtures'),)
TESTFILES_DIR = os.path.join(PROJECT_DIR, '../testfiles')
TEMPLATE_DIRS = (os.path.join(PROJECT_DIR, '../templates'),)
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, '../static'), os.path.join(PROJECT_DIR, '../media'), )
STATIC_ROOT = os.path.join(PROJECT_DIR, '../sitestatic')
MEDIA_ROOT = os.path.join(PROJECT_DIR, '../media')
MEDIA_URL = "/media/"

#-----------------------------------------------------------------------------------
# Permission Management
#-----------------------------------------------------------------------------------

# this lets us easily create new permissions across our objects
PERMISSIONS = {
    '*': ('create', # can create an object
          'read',   # can read an object, viewing it's details
          'update', # can update an object
          'delete', # can delete an object,
          'list'),  # can view a list of the objects

    'dashblocks.dashblock': ('html', ),
    'orgs.org': ('choose', 'edit', 'home', 'manage_accounts', 'create_login', 'join',
                 'chat_list', 'contact_list'),
    'polls.poll': ('questions', 'responses', 'images'),
    'stories.story': ('html', 'images'),

}

# assigns the permissions that each group should have
GROUP_PERMISSIONS = {
    "Administrators": (
        'categories.category.*',
        'categories.categoryimage.*',
        'dashblocks.dashblock.*',
        'dashblocks.dashblocktype.*',
        'news.newsitem.*',
        'news.video.*',
        'orgs.org_edit',
        'orgs.org_home',
        'orgs.org_manage_accounts',
        'orgs.org_profile',
        'orgs.orgbackground.*',
        'polls.poll.*',
        'polls.pollcategory.*',
        'polls.pollimage.*',
        'polls.featuredresponse.*',
        'stories.story.*',
        'stories.storyimage.*',
        'users.user_profile',
    ),
    "Editors": (
        'categories.category.*',
        'categories.categoryimage.*',
        'dashblocks.dashblock.*',
        'dashblocks.dashblocktype.*',
        'news.newsitem.*',
        'news.video.*',
        'orgs.org_home',
        'orgs.org_profile',
        'orgs.org_contact_list',
        'orgs.org_chat_list',
        'polls.poll.*',
        'polls.pollcategory.*',
        'polls.pollimage.*',
        'polls.featuredresponse.*',
        'stories.story.*',
        'stories.storyimage.*',
        'users.user_profile',
    ),
}

#-----------------------------------------------------------------------------------
# Login / Logout
#-----------------------------------------------------------------------------------
LOGIN_URL = "/users/login/"
LOGOUT_URL = "/users/logout/"
LOGIN_REDIRECT_URL = "/manage/org/choose/"
LOGOUT_REDIRECT_URL = "/"

#-----------------------------------------------------------------------------------
# Guardian Configuration
#-----------------------------------------------------------------------------------

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
)

ANONYMOUS_USER_ID = -1

#-----------------------------------------------------------------------------------
# Django-Nose config
#-----------------------------------------------------------------------------------

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SOUTH_TESTS_MIGRATE = False

#-----------------------------------------------------------------------------------
# Debug Toolbar
#-----------------------------------------------------------------------------------

INTERNAL_IPS = ('127.0.0.1',)
