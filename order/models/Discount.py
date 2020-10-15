from django.db import models
from product.models import Product
from customuser.models import CustomUser



class Discount(models.Model):
    title = models.CharField(max_length=255)
    user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    percent = models.FloatField(default=0.0)
    expiration = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)