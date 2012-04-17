from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from .models import Work

def work_list(request, template_name='portfolio/list.haml'):
    """Work list view"""
    works = Work.get_published_works()
    return direct_to_template(request, template_name, locals())

def work_details(request, work_id, template_name='portfolio/details.haml'):
    """Work details view"""
    work = get_object_or_404(Work, pk=work_id, is_published=True)
    return direct_to_template(request, template_name, locals())
