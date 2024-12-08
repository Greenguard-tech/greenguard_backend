from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer

class UserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
