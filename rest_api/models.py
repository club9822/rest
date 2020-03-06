from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'role', 'name', 'last_name', 'status', 'national_code',
                  'address', 'mobile', 'telephone', 'age', 'gender']
