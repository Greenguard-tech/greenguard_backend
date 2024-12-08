from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
