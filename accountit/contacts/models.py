from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import Company

class Contact(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=256)
    identification = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_customer = models.BooleanField()
    is_provider = models.BooleanField()

    def get_absolute_url(self):
        return reverse('contacts:detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name

