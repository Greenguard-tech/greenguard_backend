from django.db import models
from users.models import User  # Import User model to associate subscriptions with users
from datetime import datetime

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Subscription for {self.user.username} - {'Active' if self.is_active else 'Canceled'}"
