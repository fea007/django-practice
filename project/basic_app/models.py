from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    # Basically copying everything from the initial User Model
    # (initially created in admin interface)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Now adding new fields
    portfolio_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True)
    # blank = True means that there is
    # no requirement to fill in the field

    def __str__(self):
        return self.user.username
