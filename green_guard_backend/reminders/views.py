from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderListView(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
