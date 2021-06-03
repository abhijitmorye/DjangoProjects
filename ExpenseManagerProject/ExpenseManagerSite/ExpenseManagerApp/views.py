from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expenses

# Create your views here.


def index(request):
    if request.method == 'POST':
        expenseName = request.POST.get('expenseName')
        expenseAmount = request.POST.get('expenseAmount')
        expenseCategory = request.POST.get('expenseCategory')
        expenseDate = request.POST.get('expenseDate')

        expense = Expenses(expenseName=expenseName, expenseAmount=expenseAmount,
                           expenseCategory=expenseCategory, expenseDate=expenseDate)
        expense.save()
        return redirect('/')

    return render(request, 'ExpenseManagerApp/index.html')
