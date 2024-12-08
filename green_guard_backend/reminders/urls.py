from django.urls import path
from .views import ReminderListView

urlpatterns = [
    path('', ReminderListView.as_view(), name='reminder-list'),
]
