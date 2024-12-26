from django.shortcuts import render
from .models import ReportData

def reports_home(request):
    data = ReportData.objects.all()
    labels = [d.name for d in data]
    values = [d.value for d in data]
    return render(request, 'reports/reports_home.html', {
        'labels': labels,
        'values': values,
        'data': data
    })
