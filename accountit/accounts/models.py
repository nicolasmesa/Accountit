from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class User(AbstractUser):
    def __str__(self):
        return "{}".format(self.username)

class Company(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(blank=True, max_length=256)
    phone = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.name


class UserDetails(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='user_details')
    company = models.ForeignKey(Company, related_name='users', editable=False)
    name = models.CharField(blank=True, max_length=256)

    def __str__(self):
        return self.user.username
