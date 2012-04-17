import os, sys

sys.path[0:0] = [
    '/mnt/store/gbweb/web/django/doppler/eggs/South-0.7.4-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/django_grappelli-2.3.8-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/django_filebrowser-3.4.2-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/django_rosetta-0.6.6-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/ipython-0.12-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/simplejson-2.5.0-py2.6-linux-x86_64.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/Pygments-1.5-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/hamlpy-0.80.4-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/djaml-1.0-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/WebTest-1.3.3-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/django_webtest-1.5.2-py2.6.egg',
    '/usr/local/lib/python2.6/dist-packages',
    '/mnt/store/gbweb/web/django/doppler/eggs/django_coverage-1.2.2-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/django_any-0.2.0-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/django_jenkins-0.12.1-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/djangorecipe-1.1.2-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/Django-1.4-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/zc.recipe.egg-1.3.2-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/zc.buildout-1.5.2-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/WebOb-1.2b3-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/eggs/setuptools-0.6c12dev_r88846-py2.6.egg',
    '/mnt/store/gbweb/web/django/doppler/parts/django',
    '/mnt/store/gbweb/web/django/doppler',
]


os.environ['DJANGO_SETTINGS_MODULE'] = 'doppler.staging'
os.environ['PYTHON_EGG_CACHE'] = '/tmp/python-eggs'

import django.core.handlers.wsgi

_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    return _application(environ, start_response)
