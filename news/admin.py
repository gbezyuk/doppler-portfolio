from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from news.models import NewsItem

class NewsItemAdmin(admin.ModelAdmin):

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/grappelli/tinymce_setup/tinymce_setup.js',
		]

	save_on_top     = True
	list_per_page = 100

	date_hierarchy = 'published_at'

	list_display    = (
		'id',
		'__unicode__',
		'caption',
		'is_published',
		'published_at',
		'created_at',
		'updated_at',
	)
	list_editable = (
		'caption',
		'is_published',
	)
	list_filter = (
		'is_published',
	)
	list_per_page = 50

	search_fields = (
		'id',
		'caption',
		'announcement',
		'full_text'
	)

	def make_published(self, request, queryset):
		queryset.update(is_published=True)
	make_published.short_description = _('publish selected news')

	def make_unpublished(self, request, queryset):
		queryset.update(is_published=False)
	make_unpublished.short_description = _('unpublish selected news')

	actions = [
		make_published,
		make_unpublished,
	]

admin.site.register(NewsItem, NewsItemAdmin)