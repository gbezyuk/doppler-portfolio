from django.utils.translation import ugettext_lazy as _
from django.contrib.syndication.views import Feed
from news.models import NewsItem

class NewsFeed(Feed):
	title = _('Doppler studio news')
	link = "/news/"
	description = _('Doppler studio news')

	def items(self):
		return NewsItem.get_actual_news()

	def item_title(self, item):
		return item.caption

	def item_description(self, item):
		return item.full_text