from django.conf.urls.defaults import patterns, url
from django.views.generic import list_detail
from django.views.generic.simple import redirect_to, direct_to_template
from .models import NewsItem
from .feed import NewsFeed

queryset = NewsItem.get_actual_news()

urlpatterns = patterns('',
	url(r'^$', redirect_to, { 'url': '/news/list' }, name='index'),
	url(r'list$',
		list_detail.object_list,
		{
			'queryset': queryset,
		    'template_name': 'news/newsitem_list.haml'
		},
		name='list'),
	url(r'(?P<object_id>\d+)/$',
		list_detail.object_detail,
		{
			'queryset': queryset,
			'template_name': 'news/newsitem_detail.haml'
		},
		name='detail'),
	url(r'^feed/$', NewsFeed(), name='feed'),
)
