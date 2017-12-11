from rest_framework import serializers
from . import models


class ItemSoldSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.ItemSold
        fields = ('item', 'name', 'quantity', 'price', 'tax', 'observations', )
        extra_kwargs = {
            'item': {'view_name': 'items:item-detail'},
        }


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    itemsold_set = ItemSoldSerializer(many=True)

    class Meta:
        model = models.Invoice
        fields = ('url', 'contact', 'code', 'creation_date', 'expiration_date', 'observations', 'itemsold_set', )
        extra_kwargs = {
            'url': {'view_name': 'invoices:invoice-detail'},
            'contact': {'view_name': 'contacts:contact-detail'},
        }

    def create(self, validated_data):
        items_data = validated_data.pop('itemsold_set')
        invoice = models.Invoice.objects.create(**validated_data)

        company = validated_data['company']

        for item_data in items_data:
            models.ItemSold.objects.create(invoice=invoice, company=company, **item_data)

        return invoice

    # TODO: Should be transactional
    def update(self, instance, validated_data):
        # Remove all items sold
        for item_to_delete in instance.itemsold_set.all():
            item_to_delete.delete()

        items_data = validated_data.pop('itemsold_set')

        company = instance.company

        invoice = models.Invoice(**validated_data)
        invoice.pk = instance.pk
        invoice.company = company
        invoice.save()

        for item_data in items_data:
            models.ItemSold.objects.create(invoice=invoice, company=company, **item_data)

        return invoice


