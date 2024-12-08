from django.db import models
from django.contrib.auth.models import User
from plants.models import Plant 

class Booking(models.Model):
    PICKUP_DROP_OFF = 'pickup_drop_off'
    HOME_SERVICE = 'home_service'
    BOOKING_TYPE_CHOICES = [
        (PICKUP_DROP_OFF, 'Pickup / Drop Off'),
        (HOME_SERVICE, 'Home Service'),
    ]
    
    PENDING = 'pending'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True)  # Allow plant to be nullable
    booking_type = models.CharField(max_length=20, choices=BOOKING_TYPE_CHOICES, default=PICKUP_DROP_OFF)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.id} for {self.plant} by {self.user.username}"
