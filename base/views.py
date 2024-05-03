from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AlgobullsEmployee
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
def home(request):
    try:
        algobulls_employee = AlgobullsEmployee.objects.get(email_id=request.user.username)
        employee_id = algobulls_employee.employee_id
    except AlgobullsEmployee.DoesNotExist:
        employee_id = None

    user_groups = request.user.groups.all()

    context = {
        'user_groups': user_groups,
        'employee_id': employee_id,
    }

    return render(request, 'base.html', context)
