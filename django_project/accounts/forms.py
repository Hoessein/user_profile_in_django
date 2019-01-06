from django import forms

from django.contrib.auth.models import User

from .models import Profile

from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm


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
        """Checks if email1 and email2 are the same"""
        cleaned_data = super().clean()
        email = cleaned_data['email']
        confirm = cleaned_data['confirm_email']
        if email != confirm:
            raise forms.ValidationError("you need to enter the same email in both fields")


class ChangePasswordForm(PasswordChangeForm):

    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        """Prevents help text to be printed"""
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].help_text = ''
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''

    def clean_old_password(self):
        """Checks if the old password entered is the actual old password"""
        cleaned_data = super().clean()
        old_password = cleaned_data['old_password']
        if not self.user.check_password(old_password):
            raise forms.ValidationError('Your old password is incorrect')


    def clean_new_password1(self):
        """Checks if old password is the same as new password"""
        new_password = self.cleaned_data['new_password1']
        old_new_password_comparison = self.user.check_password(new_password)
        if old_new_password_comparison:
            raise forms.ValidationError("Your old password can't be the same as your new password.")

        return new_password


class CreationUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username',
                  'password1',
                  'password2'
                  ]

    def __init__(self, *args, **kwargs):
        """Prevents help text to be printed"""
        super(CreationUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

