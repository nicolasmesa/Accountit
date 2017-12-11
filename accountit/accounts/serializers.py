from .models import Company
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'address', 'phone')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'is_admin', 'password', 'url',)
        model = get_user_model()
        extra_kwargs = {
            'url': {'view_name': 'accounts:user-detail'},
            'password': {'write_only': True},
            'username': {'read_only': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        updated = super().update(instance, validated_data)

        if 'password' in validated_data:
            updated.set_password(validated_data['password'])
            updated.save()
        
        return updated
        

