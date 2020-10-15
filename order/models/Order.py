from django.db import models
from product.models import Product
from customuser.models import CustomUser
from order.models.Cart import Cart


class Order(models.Model):
    product_id = models.ForeignKey(to=Product, related_name='order', on_delete=models.CASCADE, )
    user_id = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} محصول ".format(Product.objects.get(id=self.product_id))
