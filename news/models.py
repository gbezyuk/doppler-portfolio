from django.utils.translation import ugettext_lazy as _
from django.db import models
from datetime import datetime

class NewsItem(models.Model):
	class Meta():
		verbose_name = _(u'news item')
		verbose_name_plural = _(u'news items')
		ordering = ('published_at',)

	caption = models.CharField(max_length=300, default='', blank=False, null=False, verbose_name=_(u'caption'))
	announcement = models.TextField(default='', blank=True, null=True, verbose_name=_(u'announcement'))
	full_text = models.TextField(default='', blank=True, null=True, verbose_name=_(u'full text'))
	is_published = models.BooleanField(default=False, verbose_name=_(u'is published'))
	published_at = models.DateTimeField(verbose_name=_(u'published at'))
	updated_at = models.DateTimeField(auto_now = True, verbose_name	= _('updated at'),)
	created_at = models.DateTimeField(auto_now_add = True, verbose_name	= _('created at'),)

	def __unicode__(self):
		return self.caption

	@models.permalink
	def get_absolute_url(self):
		return ('news:detail', (), { 'object_id': self.pk })

	@classmethod
	def get_actual_news(cls):
		return NewsItem.objects.filter(is_published=True).filter(published_at__lt=datetime.now()).order_by('-published_at')