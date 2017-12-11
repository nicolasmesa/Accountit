from rest_framework.serializers import HyperlinkedModelSerializer
from . import models


class ContactSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.Contact
        fields = ('url', 'name', 'identification', 'phone', 'address', 'email', 'is_customer', 'is_provider',)
        extra_kwargs = {
            'url': {'view_name': 'contacts:contact-detail'},
        }

