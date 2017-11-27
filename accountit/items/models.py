from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import Company


class Item(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=256)
    price = models.FloatField()
    tax = models.FloatField()
    observations = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('items:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
