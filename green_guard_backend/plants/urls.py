from django.urls import path
from .views import PlantListCreateView, PlantRetrieveUpdateDestroyView

urlpatterns = [
    path('', PlantListCreateView.as_view(), name='plant-list-create'),
    path('<int:pk>/', PlantRetrieveUpdateDestroyView.as_view(), name='plant-detail'),
]
