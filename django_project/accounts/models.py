from django.db import models

from django.contrib.auth.models import User
from django.core import validators
from PIL import Image


class Profile(models.Model):
    # if the user is the deleted the profile will be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='haha@haha.nl')
    confirm_email = models.EmailField(default='haha@haha.nl')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField(null=True)
    bio = models.TextField(validators=[validators.MinLengthValidator(10)])
    avatar = models.ImageField(upload_to='profile_pics', default='default.jpg')

    # (YYYY-MM-DD, MM / DD / YYYY, or MM / DD / YY)
    # '%Y-%m-%d',
    # '%m / %d / %Y',
    # '%m / %d / %y'

    def __str__(self):
        """If the models is looked up it will print the username of the user"""
        return self.user.username

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.avatar.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.avatar.path)