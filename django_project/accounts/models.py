from django.db import models

from django.contrib.auth.models import User
from django.core import validators


class Profile(models.Model):
    # if the user is the deleted the profile will be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default="")
    confirm_email = models.EmailField(default="")
    first_name = models.CharField(default="", max_length=250)
    last_name = models.CharField(default="", max_length=250)
    date_of_birth = models.DateField(null=True)
    bio = models.TextField(validators=[validators.MinLengthValidator(10)])
    avatar = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        """Prints username from database as string"""
        return self.user.username
