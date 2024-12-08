from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    # nursery = models.ForeignKey('nurseries.Nursery', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
