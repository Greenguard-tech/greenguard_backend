from django.db import models

class Booking(models.Model):
    TYPE_CHOICES = [
        ('pickup', 'Pickup/Drop'),
        ('home_service', 'Home Service'),
    ]
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    nursery = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='nursery_bookings')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date = models.DateField()
    status = models.CharField(max_length=20, default='pending')
    payment_status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)



