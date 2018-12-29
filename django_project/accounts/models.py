from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    # if the user is the deleted the profile will be deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    bio = models.TextField()
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        """If the models is looked up it will print the username of the user"""
        return self.user.username




