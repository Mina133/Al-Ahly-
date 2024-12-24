from django.db import models
from Members.models import Member

class Subscription(models.Model):
    plan_type = models.CharField(max_length=20, choices=[
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly')
    ])
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='subscriptions')

    def __str__(self):
        return f"{self.member.name} - {self.plan_type}"
