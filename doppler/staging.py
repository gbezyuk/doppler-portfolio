from doppler.settings import *

DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
PROJECT_ROOT = '/home/gbezyuk/d/web/django/doppler/'
SITE_ROOT = PROJECT_ROOT + 'doppler/'
MEDIA_ROOT = SITE_ROOT + 'media/'
STATIC_ROOT = SITE_ROOT + 'static/'
EMAIL_FILE_PATH = PROJECT_ROOT +  'mail_dump/'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': PROJECT_ROOT + 'staging.sqlite3',
	}
}

ADMINS = (('Grigory Bezyuk', 'gbezyuk@gmail.com'))
MANAGERS = ADMINS
