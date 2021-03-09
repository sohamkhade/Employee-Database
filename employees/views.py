from django.shortcuts import render
from django.http import Http404
from .models import Employees

# Create your views here.


def home(request):
    employees = Employees.objects.all()
    return render(request, 'home.html', {'employees': employees})


def employee_detail(request, employee_id):
    try:
        employee = Employees.objects.get(id=employee_id)
    except Employees.DoesNotExist:
        raise Http404('Employee not found')
    return render(request, 'employee_detail.html', {'employee': employee})
