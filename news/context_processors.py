from news.models import NewsItem
import datetime

def news(request):
	now=datetime.datetime.now()
	return {
		'news': NewsItem.objects.filter(is_published=True).filter(published_at__lt=now).order_by('-published_at')[:3],
		'request': request
	}