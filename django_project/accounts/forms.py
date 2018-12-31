from django import forms

from django.contrib.auth.models import User
from django.contrib.admin import widgets
from django.core import validators
from .models import Profile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name',
                  'last_name',
                  'email',
                  'confirm_email',
                  'date_of_birth',
                  'bio',
                  'avatar'
                  ]

    def clean(self):
        """If the """
        cleaned_data = super().clean()
        email = cleaned_data['email']
        confirm = cleaned_data['confirm_email']
        if email != confirm:
            raise forms.ValidationError(
                "you need to enter the same email in both fields")
