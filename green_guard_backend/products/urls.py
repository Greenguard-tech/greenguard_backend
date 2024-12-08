from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),  # List and create products
    path('<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),  # Retrieve, update, or delete a specific product
    path('category/<str:category>/', ProductListCreateView.as_view(), name='product-category-list'),  # Filter by product category
]
