from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User


# class AbstractUser(User):
#     role = models.CharField(max_length=25)
#
#     class Meta:
#         ordering = ['id']


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email']
        #
#         'role', 'first_name', 'last_name', 'status', 'national_code',
#                   'address', 'mobile', 'telephone', 'age', 'gender']

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = AbstractUser
#         fields = '__all__'
