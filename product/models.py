from django.db import models
from rest_framework import serializers
from user.models import User


#
#
#
#

class ProductCategory(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    parent = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=25)
    creator = models.ForeignKey(to=User, related_name='productcategory', on_delete=models.CASCADE, default=1)
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
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    status = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
