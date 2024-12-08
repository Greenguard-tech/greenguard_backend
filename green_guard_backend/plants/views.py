from rest_framework import generics
from .models import Plant
from .serializers import PlantSerializer

class PlantListCreateView(generics.ListCreateAPIView):
    queryset = Plant.objects.filter(is_available=True)  # Filter to only available plants
    serializer_class = PlantSerializer

    def perform_create(self, serializer):
        # Optionally handle any custom logic during creation
        serializer.save()

class PlantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
