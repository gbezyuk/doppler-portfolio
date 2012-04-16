from django.conf.urls.defaults import patterns, include, url
from portfolio.views import *

urlpatterns = patterns('',
    url(r'^$', work_list, name='work_list'),
    url(r'^(?P<work_id>\d+)/$', work_details, name='work_details'),
)