from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()

# View for registering a new user
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

# View for logging in a user and getting JWT token
class UserLoginView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to access login

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']  # Extract user from validated data
            refresh = RefreshToken.for_user(user)  # Generate refresh token
            return Response({
                'access': str(refresh.access_token),  # Return access token
                'refresh': str(refresh),  # Return refresh token
            })
        return Response(serializer.errors, status=400)  # Return error if invalid
    
# View to list all users (Admin only)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAdminUser]

# View to get details of a specific user (Authenticated user or Admin)
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

# View to update a user's data (Authenticated user or Admin)
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

# View to delete a user (Admin only)
class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.IsAdminUser]