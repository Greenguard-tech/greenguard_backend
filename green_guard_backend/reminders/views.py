from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer

# View to list all reminders and create a new reminder
class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

# View to retrieve, update, or delete a specific reminder
class ReminderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
