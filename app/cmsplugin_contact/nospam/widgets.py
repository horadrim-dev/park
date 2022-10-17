from django import forms
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe


# Honeypot widget -- most automated spam posters will check any checkbox
# assuming it's an "I accept terms and conditions" box
class HoneypotWidget(forms.CheckboxInput):
    is_hidden = True

    def render(self, *args, **kwargs):
        wrapper_html = u'<div style="display: none;"><label for="id_accept_terms">%s</label>%%s</div>' % (_('Are you a robot?'))
        return mark_safe(wrapper_html % super(HoneypotWidget, self).render(*args, **kwargs))
