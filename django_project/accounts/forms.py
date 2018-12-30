from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
                  'date_of_birth',
                  'confirm_email',
                  'bio',
                  'avatar'
                  ]

