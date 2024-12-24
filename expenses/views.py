from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form})

