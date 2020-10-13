from rest_framework import viewsets
from product.models import Product, ProductCategory
from product.serializers import ProductSerializer, ProductCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_queryset(self):
    #     """
    #     overright get method
    #     :return:
    #     """
    #   return self.queryset.filter(user=self.request.user)

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
