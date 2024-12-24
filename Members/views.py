from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from .forms import MemberForm

def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'members/member_form.html', {'form': form})