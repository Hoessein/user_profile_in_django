from django import forms

from django.contrib.auth.models import User
from django.contrib.admin import widgets
from django.core import validators
from .models import Profile

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password


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


class ChangePasswordForm(PasswordChangeForm):

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''


    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        cleaned_data = super().clean()
        old_password = cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Your old password is incorrect')

