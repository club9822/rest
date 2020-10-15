from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User, PermissionsMixin


# class AbstractUser(User):
#     role = models.CharField(max_length=25)
#
#     class Meta:
#         ordering = ['id']


class CustomUserManager(BaseUserManager):
    def create_user(self, mobile, password=None, status="active", **extra_fields):
        """
        create custom customuser manager
        mobile is required
        :param status:
        :param mobile:
        :param password:
        :param extra_fields:
        :return: customuser
        """
        if not mobile:
            raise ValueError(_('The mobile must be set'))
        user = self.model(mobile=mobile, status=status, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, mobile, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('national_id', '')
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(mobile=mobile, password=password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=15, unique=True)
    national_id = models.CharField(max_length=15, default='')
    status = models.CharField(max_length=15, default="active")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'mobile'
    objects = CustomUserManager()

    def __str__(self):
        return self.mobile


# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = '__all__'
#         fields = ['id', 'url', 'username', 'password', 'email', 'is_staff', 'first_name', 'last_name']
#
#         'role', 'first_name', 'last_name', 'status', 'national_code',
#                   'address', 'mobile', 'telephone', 'age', 'gender']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
