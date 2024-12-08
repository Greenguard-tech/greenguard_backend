from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

# View to list all bookings and create a new booking
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# View to retrieve, update, or delete a booking
class BookingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
