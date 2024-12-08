from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

# View to list all products and create a new product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# View to retrieve, update, or delete a specific product
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
