from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import Company
from contacts.models import Contact
from items.models import Item

class Invoice(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)
    items = models.ManyToManyField(Item, through='ItemSold', through_fields=('invoice', 'item'))
    code = models.CharField(max_length=256)
    creation_date = models.DateField()
    expiration_date = models.DateField()
    observations = models.TextField(null=True, blank=True)

    def get_total(self):
        total = 0;
        for item_sold in self.itemsold_set.all():
            total += item_sold.get_total()
        return total

    def get_absolute_url(self):
        return reverse('invoices:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "Invoice: {}".format(self.contact)


class ItemSold(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)

    quantity = models.PositiveIntegerField()

    name = models.CharField(max_length=256)
    price = models.FloatField()
    tax = models.FloatField()
    observations = models.TextField(null=True, blank=True)

    def get_total(self):
        return self.price * self.quantity * (1 + self.tax /100.0)

    def __str__(self):
        return "{} - Value: ${}".format(self.name, self.get_total())

