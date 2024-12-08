from rest_framework import serializers
from .models import Reminder
from plants.models import Plant

class ReminderSerializer(serializers.ModelSerializer):
    plant = serializers.PrimaryKeyRelatedField(queryset=Plant.objects.all())

    class Meta:
        model = Reminder
        fields = ['id', 'plant', 'message', 'reminder_time', 'is_completed']
