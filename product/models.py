from django.db import models


#
#
#
#
class ProductCategory(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    parent: models.IntegerField(default=None)

    class Meta:
        ordering = ['created']


#
#
#
#
class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField
    category: models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
