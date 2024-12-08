from django.db import models

class Product(models.Model):
    SEED = 'seed'
    PLANT = 'plant'
    MANURE = 'manure'
    CATEGORY_CHOICES = [
        (SEED, 'Seed'),
        (PLANT, 'Plant'),
        (MANURE, 'Manure'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=PLANT)
    is_available = models.BooleanField(default=True)
    
    # Optional: Could add a field to link products to a nursery (if you later implement the nursery app)
    # nursery = models.ForeignKey('nurseries.Nursery', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
