# -*- coding: utf-8 -*-
import os
import sys
import posixpath
from datetime import timedelta


gettext = lambda s: s
_ = gettext


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# add to python-path
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'tools'))
sys.path.insert(0, os.path.join(BASE_DIR, 'cmsplugins'))
sys.path.insert(0, os.path.join(BASE_DIR, 'ecommerce'))


SECRET_KEY = 'j1odx#ji=z%r@in1k3pj4=&kwgv&4dv78^9!nymh+vhy9m4&e*'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []

SITE_ID = 1

BASE_SITE_ID = 1


LOCALE_PATHS = ('%s/locale/' % BASE_DIR,)

# Internationalization
LANGUAGE_CODE = 'de-ch'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('de-ch', _('German')),
    ('en', _('English')),
]

CMS_LANGUAGES = {
    1: [
        {
            'code': 'de-ch',
            'name': _('German'),
            'public': True,
            'redirect_on_fallback': False,
        },
        {
            'code': 'en',
            'name': _('English'),
            'fallbacks': ['de-ch',],
            'public': True,
        },
    ],
    'default': {
        'fallbacks': ['en', 'de-ch',],
        'redirect_on_fallback': False,
        'public': False,
        'hide_untranslated': False,
    }
}

PARLER_DEFAULT_LANGUAGE_CODE = 'de-ch'
PARLER_LANGUAGES = {
    # Global site
    1: (
        {'code': 'de-ch',},
        {'code': 'en',},
    ),
    'default': {
        'hide_untranslated': False,
    }
}

SOLID_I18N_USE_REDIRECTS = False

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'


# Application definition

INSTALLED_APPS = (


    'djangocms_admin_style',
    'admin_shortcuts',
    # django base
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'solid_i18n',
    'alogin',

    # wip only
    'django.contrib.webdesign',


    # life-savers
    'crispy_forms',
    'raven.contrib.django.raven_compat',
    'tastypie',
    'kombu.transport.django',
    'relatedadminlink',

    'remoteauth',

    # cms
    'cms',
    'mptt',
    'treebeard', # mptt replacement for cms
    'menus',
    'sekizai',
    # cms extension
    #'pagesetting',
    # cms plugins
    #'cms.plugins.file',
    #'cms.plugins.link',
    #'cms.plugins.text',
    #'cms.plugins.video',
    #'cms.plugins.snippet',
    # cms / filer

    'djangocms_picture',
    'djangocms_link',

    'filer',
    'cmsplugin_filer_file',
    #'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    #'cmsplugin_filer_teaser',
    #'cmsplugin_filer_video',

    'turbolinks',
    'nunjucks',

    # new-school-plugins
    'djangocms_text_ckeditor',
    'apiproxy',
    'pushy_client',

    'django_extensions',
    'compressor',
    'easy_thumbnails',
    'analytics',
    'absolute',
    'emailit',
    'hvad',
    'colorfield',
    'geoposition',

    'base',
    'bplayer',
    'achat',
    'onair',
    'backfeed',
    'stationtime',
    'remotelink',
    'contentproxy',
    'profiles',
    'ticker',
    'social_auth',

    # shop
    #'plata',
    #'plata.discount',
    #'plata.payment',
    #'plata.shop',

)

AUTH_USER_MODEL = 'remoteauth.User'

REGISTRATION_SUPPLEMENT_CLASS = 'wholesale.models.DealerRegistration'
REGISTRATION_DJANGO_AUTH_URL_NAMES_PREFIX = 'auth_'
REGISTRATION_DEFAULT_PASSWORD_LENGTH = 14

MIDDLEWARE_CLASSES = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'turbolinks.middleware.TurbolinksMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'solid_i18n.middleware.SolidLocaleMiddleware',
    #'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    # /cms

    # cms ajax-loader redirect
    'base.middleware.AJAXLoaderRedireckMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_auth.middleware.SocialAuthExceptionMiddleware',
    'django_downloadview.SmartDownloadMiddleware',
)

"""
CKEDITOR_SETTINGS = {
    'skin': 'moono',
}
"""

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data.sqlite3'),
    }
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# TASKS
CELERYBEAT_SCHEDULE = {
    'onair-update-schedule': {
        'task': 'onair.tasks.update_schedule',
        'schedule': timedelta(seconds=60),
        'kwargs': {'range_start': 600, 'range_end': 600}
    },
    'onair-cleanup-schedule': {
        'task': 'onair.tasks.cleanup_schedule',
        'schedule': timedelta(seconds=60*60),
        'kwargs': {'max_age': 12*60*60}
    },
    'contentproxy-cleanup-cache': {
        'task': 'contentproxy.tasks.cleanup_cache',
        'schedule': timedelta(seconds=60*60),
        'kwargs': {'max_age': 12*60*60}
    },
}




# auth
AUTHENTICATION_BACKENDS = (
    # social-auth
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.contrib.dropbox.DropboxBackend',
    'social_auth.backends.contrib.soundcloud.SoundcloudBackend',
    # remote api auth
    'remoteauth.backends.RemoteUserBackend',
)

LOGIN_ERROR_URL = '/'


ANONYMOUS_USER_ID = -1
ACCOUNT_ACTIVATION_DAYS = 7

CMS_GIT_FILE = os.path.join(BASE_DIR, 'changelog.txt')
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    #'django_jenkins.tasks.django_tests',
    #'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
)


# registration
ACCOUNT_ACTIVATION_DAYS = 7

# Apps to run ci-tests on
PROJECT_APPS = (
    # 'my_app',
)

SETTINGS_EXPORT = [
    'DEBUG',
    'API_BASE_URL',
    'STREAM_URL',
    'STATIC_BASE_URL',
    'ONAIR_LOAD_HISTORY',
]

ADMIN_SHORTCUTS = [
    {
        'title': _('Quick Links'),
        'shortcuts': [
            {
                'url': '/',
                'title': _('Public Site'),
                'open_new_window': True,
            },
            {
                'url': 'https://lab.hazelfire.com/projects/openbroadcast-ch/activity',
                'title': _('Bug- & Issue Tracker'),
                'open_new_window': True,
                'class': 'tool',
            },
            #{
            #    'url': 'https://pbinteractive.teamwork.com/projects/96606/overview',
            #    'title': _('Teamwork PM'),
            #    'open_new_window': True,
            #    'class': 'tool',
            #},

        ]
    },
    {
        'title': _('Administration'),
        'shortcuts': [
            {
                'url_name': 'admin:cms_page_changelist',
                'title': _('CMS Pages'),
            },

            #{
            #    'url_name': 'admin:catalog_product_changelist',
            #    'title': _('Products'),
            #    'class': 'tool',
            #},
            #{
            #    'url_name': 'admin:stories_story_changelist',
            #    'title': _('Stories'),
            #    'class': 'tool',
            #},
        ]
    },
]

BADBROWSER_REQUIREMENTS = (
	("firefox", "22.0"),
	("chrome", "22.0"),
	("microsoft internet explorer", "11.0"),
	("opera", None),
)
BADBROWSER_SUGGEST = ('chrome', 'safari', 'ie', 'firefox', )


#LOGIN_REDIRECT_URL = '/accounts/contact/'
LOGIN_REDIRECT_URL = '/'

# shop
#PLATA_SHOP_PRODUCT = 'catalog.Combo'
CURRENCIES = ('CHF', 'EUR',)

#PLATA_PAYMENT_MODULES = [
    #'plata.payment.modules.cod.PaymentProcessor',
    #'bshop.payment.postpay.PaymentProcessor',
    #'plata.payment.modules.paypal.PaymentProcessor',
#]

#PLATA_REPORTING_ADDRESSLINE = 'Example Corp. - 3. Example Street - 1234 Example'

PAYPAL = {
    'LIVE': False, # Use sandbox or live payment interface?
    'BUSINESS': 'paypal@example.com',
    }