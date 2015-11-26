# -*- coding: utf-8 -*-
from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['fullname', 'email']

    def clean_email(self):
        print self.cleaned_data.get('email')     # Выводит в консоль всю информацию
        email_base, provider = self.cleaned_data.get('email').split('@')
        domain, extension = provider.split('.')
        # if not 'edu' in self.cleaned_data.get('email')
        # if not domain == 'USC':
        #     raise forms.ValidationError('Please make sure you use your USC email')
        if not extension == 'com':
            raise forms.ValidationError('Please use a \'.com\' in email')
        return 'test@test.com'      # При успешной регистрации сохранят этот адресс
        # email = self.cleaned_data.get('email')
        # return email

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        # write validation code
        return fullname


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=200, required=False)

    def clean_email(self):
        email_base, provider = self.cleaned_data.get('email').split('@')
        domain, extension = provider.split('.')

        if not extension == 'com':
            raise forms.ValidationError('Please use a \'.com\' in email')

        return self.cleaned_data.get('email')
