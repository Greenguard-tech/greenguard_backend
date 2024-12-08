from django.db import models
from plants.models import Plant  # Import Plant model to associate reminders with plants

class Reminder(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    reminder_time = models.DateTimeField(null=True,blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder for {self.plant.name} - {self.message}"
