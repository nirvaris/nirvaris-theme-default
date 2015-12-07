from django import forms

from django.utils.translation import ugettext as _


class FormStyleForm(forms.Form):

    name = forms.CharField(required=True, label=_('Name'), max_length=200)
    email = forms.EmailField(required=True, label=_('E-mail address'))
    message = forms.CharField(required=True, label=_('Message'), max_length=200, widget=forms.Textarea)
    send_to_me = forms.BooleanField(label=_('Check me or not'))

    anti_spam_token = forms.CharField(widget=forms.HiddenInput())
    anti_spam_hidden = forms.CharField(widget=forms.HiddenInput())
    anti_spam_no_hidden = forms.CharField(required=False,label='')
     
    def clean(self):
        cleaned_data = super(FormStyleForm, self).clean()

        if 'name' in cleaned_data:
            if 'form_top_message' in cleaned_data['name']:
                    self.add_error(None,_('Top message error'))
        
        return cleaned_data
        

    def anti_spam(self):
        
        spam_token = uuid.uuid4()
        
        self.initial['anti_spam_token'] = str(spam_token)
        self.initial['anti_spam_no_hidden'] = str(spam_token) 
        self.initial['anti_spam_hidden'] = ''  