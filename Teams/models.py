from django.db import models

# Create your models here.
from django.db import models
from Members.models import Member

class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name='coached_teams')

    def __str__(self):
        return self.name