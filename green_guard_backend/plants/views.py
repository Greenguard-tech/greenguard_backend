from rest_framework import generics
from .models import Plant
from .serializers import PlantSerializer

class PlantListView(generics.ListAPIView):
    queryset = Plant.objects.filter(is_available=True)
    serializer_class = PlantSerializer
