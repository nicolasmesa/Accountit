from rest_framework import serializers
from . import models


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Item
        fields = ('name', 'price', 'tax', 'observations', 'url',)
        extra_kwargs = {
            'url': {'view_name': 'items:item-detail'},
        }

