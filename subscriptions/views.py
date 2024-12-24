from django.shortcuts import render, redirect
from .models import Subscription
from .forms import SubscriptionForm

def subscription_list(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'subscriptions/subscription_list.html', {'subscriptions': subscriptions})

def subscription_create(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription_list')
    else:
        form = SubscriptionForm()
    return render(request, 'subscriptions/subscription_form.html', {'form': form})
