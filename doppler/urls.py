from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from doppler.views import *
from filebrowser.sites import site
from django.conf import settings
admin.autodiscover()

handler404 = ViewFor404.as_view()
handler500 = ViewFor500.as_view()

urlpatterns = patterns('',
#    Examples:
#    url(r'^$', 'tulius.views.home', name='home'),
#    url(r'^tulius/', include('tulius.foo.urls')),

#    url(r'^smart_selects/', include('smart_selects.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/rosetta/', include('rosetta.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('accounts.urls')),
#	url(r'^accounts/profile/', include('tulius.profile.urls')),

	url(r'^$', HomeView.as_view(), name='home'),
    url(r'^news/', include('news.urls',  namespace='news')),
    url(r'^portfolio/', include('portfolio.urls',)),
    url(r'^flatpages/', 'flatpages.views.list',  name='flatpages'),
#	url(r'^plots/', include('tulius.plots.urls',  namespace='plots')),
#	url(r'^games/', include('tulius.games.urls',  namespace='games')),
#	url(r'^forums/', include('tulius.forum.urls',  namespace='forum')),
)


if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			 {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve',
			 {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
	)
