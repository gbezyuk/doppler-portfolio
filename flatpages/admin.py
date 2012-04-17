from django.contrib import admin
from .models import FlatPage
from .forms import FlatpageAdminForm

class FlatPageAdmin(admin.ModelAdmin):
	form = FlatpageAdminForm

	class Media:
		js = [
			'/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
			'/static/grappelli/tinymce_setup/tinymce_setup.js',
			]

	save_on_top     = True
	list_per_page = 100
	    
	date_hierarchy = 'created_at'

	list_display = (
		'__unicode__',
		'url',
		'title',
		'is_enabled',
	)
	list_display_links = (
		'__unicode__',
	)
	list_editable = (
		'url',
		'title',
		'is_enabled',
	)
	list_filter = (
	)
	search_fields = (
		'url',
		'title',
	)

admin.site.register(FlatPage, FlatPageAdmin)
