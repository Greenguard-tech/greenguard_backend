from rest_framework import serializers
from .models import Subscription
from users.models import User  # To associate the user

class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'start_date', 'end_date', 'is_active']
