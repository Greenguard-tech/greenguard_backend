from django.urls import path
from .views import BookingListCreateView, BookingRetrieveUpdateDestroyView

urlpatterns = [
    path('', BookingListCreateView.as_view(), name='booking-list-create'),  # List and create bookings
    path('<int:pk>/', BookingRetrieveUpdateDestroyView.as_view(), name='booking-detail'),  # Retrieve, update, or delete a specific booking
]
