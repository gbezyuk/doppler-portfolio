from django.utils.translation import ugettext_lazy as _
from .models import FlatPage
from django import forms

class FlatpageAdminForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]*/$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " dots, underscores, dashes, slashes or tildes."))
    class Meta:
        model = FlatPage
