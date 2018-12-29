from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    birthdate = forms.DateField
    confirm_email= forms.EmailField()
    short_bio = forms.Textarea()

    class Meta:
        model = User
        fields = ['username', 'lastname', 'email', 'birthdate', 'confirm_emails', 'short_bio']


