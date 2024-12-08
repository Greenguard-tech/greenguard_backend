from rest_framework import generics
from .models import Subscription
from .serializers import SubscriptionSerializer

# View to list all subscriptions and create a new subscription
class SubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

# View to retrieve, update, or delete a specific subscription
class SubscriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
