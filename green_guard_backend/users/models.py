from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLES = [
        ('user', 'User'),
        ('nursery', 'Nursery'),
        ('gardener', 'Gardener'),
    ]
    
    role = models.CharField(max_length=100, choices=[('admin', 'Admin'), ('user', 'User')], default='user')

    # Add related_name to avoid clashes with the default User model's reverse relationships
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Custom related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Custom related_name
        blank=True,
    )
    
    def _str_(self):
        return f"{self.username} ({self.role})"