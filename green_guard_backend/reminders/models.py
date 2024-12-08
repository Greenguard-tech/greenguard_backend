from django.db import models

class Reminder(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    plant = models.ForeignKey('plants.Plant', on_delete=models.CASCADE)
    reminder_time = models.TimeField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

