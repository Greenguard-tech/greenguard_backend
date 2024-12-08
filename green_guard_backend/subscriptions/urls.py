from django.urls import path
from .views import SubscriptionListCreateView, SubscriptionRetrieveUpdateDestroyView

urlpatterns = [
    path('', SubscriptionListCreateView.as_view(), name='subscription-list-create'),  # List and create subscriptions
    path('<int:pk>/', SubscriptionRetrieveUpdateDestroyView.as_view(), name='subscription-detail'),  # Retrieve, update, or delete a specific subscription
]
