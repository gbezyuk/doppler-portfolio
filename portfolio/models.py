from django.utils.translation import ugettext_lazy as _
from django.db import models

class Work(models.Model):
	class Meta():
		verbose_name = _(u'work')
		verbose_name_plural = _(u'works')
		ordering = ('-updated_at',)

	title = models.CharField(max_length=300, default='', blank=False, null=False, verbose_name=_(u'title'))
	description = models.TextField(default='', blank=True, null=True, verbose_name=_(u'description'))
	is_published = models.BooleanField(default=False, verbose_name=_(u'is published'))
	updated_at = models.DateTimeField(auto_now = True, verbose_name	= _('updated at'),)
	created_at = models.DateTimeField(auto_now_add = True, verbose_name	= _('created at'),)

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('portfolio:work_detail', (), { 'work_id': self.pk })

	@classmethod
	def get_published_works(cls):
		return cls.objects.filter(is_published=True)