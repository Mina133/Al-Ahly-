from django.db import models
from Teams.models import Team

class Expense(models.Model):
    expense_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='expenses')
    def __str__(self):
        return f"{self.expense_type} - {self.amount}"
