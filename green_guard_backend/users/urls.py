from django.urls import path
from .views import UserRegisterView, UserLoginView, UserListView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('users/', UserListView.as_view(), name='user-list'),  # Admin-only endpoint
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # Retrieve user details
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),  # Update user details
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),  # Delete a user
]