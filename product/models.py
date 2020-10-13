from django.db import models
from rest_framework import serializers
from user.models import CustomUser


#
#
#
#

class ProductCategory(models.Model):
    title = models.CharField(max_length=150, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    parent = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25)
    creator = models.ForeignKey(to=CustomUser, related_name='productcategory', on_delete=models.CASCADE, default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return '{}'.format(self.title)


#
#
#
#
class Product(models.Model):
    title = models.CharField(max_length=150, default=None)
    description = models.TextField(default=None)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    price = models.FloatField(default=0.0, verbose_name='قیمت')
    status = models.CharField(max_length=25, default='active')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title