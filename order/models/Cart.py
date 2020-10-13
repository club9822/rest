from django.db import models
from product.models import Product
from user.models import CustomUser


class Cart(models.Model):
    status = models.CharField(max_length=25, default='active')
    user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    # order_id=models.ForeignKey(to=Order,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} سفارش ".format(self.id)
