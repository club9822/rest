from django.contrib import admin
from product.models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Product, ProductAdmin)
