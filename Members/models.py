from django.db import models

# Create your models here.
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    subscription_status = models.CharField(max_length=10, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('overdue', 'Overdue')
    ])

    def __str__(self):
        return self.name
