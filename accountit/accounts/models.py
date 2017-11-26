from django.db import models
from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class Company(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(blank=True, max_length=256)
    phone = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    company = models.ForeignKey(Company, related_name='users', editable=False, null=True, blank=True)
    name = models.CharField(blank=True, max_length=256)

    def __str__(self):
        return "{}".format(self.username)
