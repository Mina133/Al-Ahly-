from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['plan_type', 'start_date', 'end_date', 'amount', 'member']
