from rest_framework import generics
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionsListView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer