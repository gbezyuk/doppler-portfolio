from .models import FlatPage
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect
from django.views.generic.simple import direct_to_template

DEFAULT_TEMPLATE = 'flatpages/default.haml'

# This view is called from FlatpageFallbackMiddleware.process_response
# when a 404 is raised, which often means CsrfViewMiddleware.process_view
# has not been called even if CsrfViewMiddleware is installed. So we need
# to use @csrf_protect, in case the template needs {% csrf_token %}.
# However, we can't just wrap this view; if no matching flatpage exists,
# or a redirect is required for authentication, the 404 needs to be returned
# without any CSRF checks. Therefore, we only
# CSRF protect the internal implementation.
def flatpage(request, url):
	"""
	Public interface to the flat page view.

	Models: `flatpages.flatpages`
	Templates: Uses the template defined by the ``template_name`` field,
		or `flatpages/default.html` if template_name is not defined.
	Context:
		flatpage
			`flatpages.flatpages` object
	"""
	if not url.endswith('/') and settings.APPEND_SLASH:
		return HttpResponseRedirect("%s/" % request.path)
	if not url.startswith('/'):
		url = "/" + url
	f = get_object_or_404(FlatPage, url__exact=url, is_enabled=True)
	return render_flatpage(request, f)

@csrf_protect
def render_flatpage(request, f):
	"""
	Internal interface to the flat page view.
	"""
	t = loader.get_template(DEFAULT_TEMPLATE)
	# To avoid having to always use the "|safe" filter in flatpage templates,
	# mark the title and content as already safe (since they are raw HTML
	# content in the first place).
	f.title = mark_safe(f.title)
	f.content = mark_safe(f.content)

	c = RequestContext(request, {
		'flatpage': f,
	})
	response = HttpResponse(t.render(c))
	populate_xheaders(request, response, FlatPage, f.id)
	return response

def list(request, template_name='flatpages/list.haml'):
	flatpages = FlatPage.objects.all()
	return direct_to_template(request, template_name, locals())
