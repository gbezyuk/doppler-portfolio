from django.conf.urls.defaults import *
from .views import *

urlpatterns = patterns('',
	url(r'^(?P<url>.*)$', flatpage, name='flatpage'),
	url(r'^flatpages/$', list, template_name='flatpages/list.haml', name='list'),
)
