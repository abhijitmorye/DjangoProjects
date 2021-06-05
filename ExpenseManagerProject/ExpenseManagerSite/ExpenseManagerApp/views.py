from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expenses

# Create your views here.


def index(request):
    flag = False
    if request.method == 'POST':
        expenseName = request.POST.get('expenseName')
        expenseAmount = request.POST.get('expenseAmount')
        expenseCategory = request.POST.get('expenseCategory')
        expenseDate = request.POST.get('expenseDate')

        expense = Expenses(expenseName=expenseName, expenseAmount=expenseAmount,
                           expenseCategory=expenseCategory, expenseDate=expenseDate)
        expense.save()
        return redirect('/')

    exepenes = Expenses.objects.all()
    total = 0
    totalFood = 0
    totalEnt = 0
    totalTravel = 0
    totalBusi = 0
    totalOther = 0
    if len(exepenes) == 0:
        pass
    else:
        flag = True
        for expense in exepenes:
            if expense.expenseCategory == 'Travel':
                totalTravel += expense.expenseAmount
            elif expense.expenseCategory == 'Food':
                totalFood += expense.expenseAmount
            elif expense.expenseCategory == 'Entertainment':
                totalEnt += expense.expenseAmount
            elif expense.expenseCategory == 'Business':
                totalBusi += expense.expenseAmount
            elif expense.expenseCategory == 'Other':
                totalOther += expense.expenseAmount
            total += expense.expenseAmount

    context = {
        "flag": flag,
        "expenses": exepenes,
        "total": total,
        'totalTravel': totalTravel,
        'totalFood': totalFood,
        'totalEnt': totalEnt,
        'totalBusi': totalBusi,
        'totalOther': totalOther
    }

    return render(request, 'ExpenseManagerApp/index.html', context=context)
