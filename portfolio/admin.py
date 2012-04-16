from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from portfolio.models import Work, Image
from django.conf import settings
import os
from filebrowser.base import FileObject
from django.contrib.contenttypes.generic import GenericTabularInline

def get_image_thumbnail_html(image):
	if image:
		image_fileobject = FileObject(image.path)
		if image_fileobject\
		   and image_fileobject.filetype == "Image" and os.path.isfile(settings.MEDIA_ROOT + image.path):
			str = '<img src="%s" />' % image_fileobject.version_generate(settings.FILEBROWSER_ADMIN_THUMBNAIL).url
			return str
		return False
	else:
		return False

def get_object_thumbnails_html(obj):
	html_bits = []
	for attached_image in obj.images.all():
		html_bit = get_image_thumbnail_html(attached_image.image)
		if html_bit:
			html_bits.append('<li style="float: left; margin: 2px; padding: 0;">' + html_bit + '</li>')
	if html_bits:
		return '<ul style="margin: 0; padding: 0; overflow: hidden; min-width: 168px; max-width: 336px;">' + ''.join(html_bits) + '</ul>'
	return _('no images')

class ImageInline(GenericTabularInline):
	model = Image

class WorkAdmin(admin.ModelAdmin):

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/grappelli/tinymce_setup/tinymce_setup.js',
		]

	save_on_top = True
	list_per_page = 100

	date_hierarchy = 'updated_at'

	list_display = (
		'id',
		'thumbnails',
		'title',
		'is_published',
		'created_at',
		'updated_at',
	)
	list_display_links = (
		'id',
		'thumbnails',
		'created_at',
		'updated_at',
	)
	list_editable = (
		'title',
		'is_published',
	)
	list_filter = (
		'is_published',
	)
	list_per_page = 50

	search_fields = (
		'id',
		'title',
		'description',
	)

	def thumbnails(self, obj):
		return get_object_thumbnails_html(obj)
	thumbnails.allow_tags = True
	thumbnails.short_description = _('attached images')

	def make_published(self, request, queryset):
		queryset.update(is_published=True)
	make_published.short_description = _('publish selected works')

	def make_unpublished(self, request, queryset):
		queryset.update(is_published=False)
	make_unpublished.short_description = _('unpublish selected works')

	actions = [
		make_published,
		make_unpublished,
	]

	inlines = [
		ImageInline,
	]

admin.site.register(Work, WorkAdmin)