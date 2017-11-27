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
    # editable=False means that the field won't show up in the Admin page. See https://docs.djangoproject.com/en/1.11/ref/models/fields/#editable
    company = models.ForeignKey(Company, editable=False, null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(blank=True, max_length=256)
    is_admin = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.username)
