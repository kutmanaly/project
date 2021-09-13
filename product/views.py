from rest_framework.generics import *
from product.models import Product
from product.serializers import ProductsListSerializer


class ProductsListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer