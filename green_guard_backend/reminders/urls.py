from django.urls import path
from .views import ReminderListCreateView, ReminderRetrieveUpdateDestroyView

urlpatterns = [
    path('', ReminderListCreateView.as_view(), name='reminder-list-create'),  # List and create reminders
    path('<int:pk>/', ReminderRetrieveUpdateDestroyView.as_view(), name='reminder-detail'),  # Retrieve, update, or delete a specific reminder
]
