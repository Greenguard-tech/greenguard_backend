from django.db import models

class Product(models.Model):
    nursery = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=50, choices=[('seeds', 'Seeds'), ('manure', 'Manure'), ('other', 'Other')])
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.CharField(max_length=255)
#     is_available = models.BooleanField(default=True)
