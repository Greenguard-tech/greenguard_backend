from rest_framework import generics
from .models import Booking
from .serializers import BookingSerializer

class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
