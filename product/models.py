from django.db import models
from rest_framework import serializers


#
#
#
#
class ProductCategory(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    parent = models.CharField(max_length=10)
    status = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


#
#
#
#
class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
