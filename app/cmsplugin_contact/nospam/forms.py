from django import forms

from ..nospam import utils
from .fields import HoneypotField


class BaseForm(forms.Form):
    
    def __init__(self, request, *args, **kwargs):
        self._request = request
        super(BaseForm, self).__init__(*args, **kwargs)


class AkismetForm(BaseForm):
    
    akismet_fields = {
            'comment_author': 'name',
            'comment_author_email': 'email',
            'comment_author_url': 'url',
            'comment_content': 'comment',
            }
    akismet_api_key = None
    
    def akismet_check(self):
        fields = {}
        for key, value in self.akismet_fields.items():
            fields[key] = self.cleaned_data[value]
        return utils.akismet_check(self._request, akismet_api_key=self.akismet_api_key, **fields)


class RecaptchaForm(BaseForm):
    pass


class HoneyPotForm(BaseForm):
    accept_terms = HoneypotField()


class SuperSpamKillerForm(RecaptchaForm, HoneyPotForm, AkismetForm):
    pass
