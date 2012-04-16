from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from filebrowser.fields import FileBrowseField

class Image(models.Model):
	class Meta():
		verbose_name = _('image')
		verbose_name_plural = _('images')
		ordering = ('-updated_at',)

	title = models.CharField(max_length=500, unique=False, blank=True, null=True, verbose_name=_('title'))
	image = FileBrowseField(max_length=500, extensions=[".jpeg", ".jpg",".png", ".gif"], blank=False, null=False, verbose_name=_('image'))
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = generic.GenericForeignKey('content_type', 'object_id')
	updated_at = models.DateTimeField(auto_now = True, verbose_name	= _('updated at'),)
	created_at = models.DateTimeField(auto_now_add = True, verbose_name	= _('created at'),)

class Work(models.Model):
	class Meta():
		verbose_name = _(u'work')
		verbose_name_plural = _(u'works')
		ordering = ('-updated_at',)

	title = models.CharField(max_length=300, default='', blank=False, null=False, verbose_name=_(u'title'))
	description = models.TextField(default='', blank=True, null=True, verbose_name=_(u'description'))
	is_published = models.BooleanField(default=False, verbose_name=_(u'is published'))
	images = generic.GenericRelation(Image, verbose_name=_('images'), blank=True, null=True)
	updated_at = models.DateTimeField(auto_now = True, verbose_name	= _('updated at'),)
	created_at = models.DateTimeField(auto_now_add = True, verbose_name	= _('created at'),)

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('portfolio_work_details', (), { 'work_id': self.pk })

	@classmethod
	def get_published_works(cls):
		return cls.objects.filter(is_published=True)