from django.db import models

class Subscription(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    gardener = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='subscriptions')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    plan_name = models.CharField(max_length=255)