from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Transaction, Category
from django import forms
from .models import Category
from .forms import CategoryForm
from .forms import BudgetForm
from .forms import TransactionForm
from .models import Budget
from django.db.models import Sum

def budget_tracking(request):
    budgets = Budget.objects.all()
    budget_data = []

    for budget in budgets:
        total_expenses = Transaction.objects.filter(
            category=budget.category,
            type='expense',
            date__range=(budget.start_date, budget.end_date)
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        budget_data.append({
            'category': budget.category.name,
            'limit': budget.limit,
            'total_expenses': total_expenses,
            'remaining': budget.limit - total_expenses
        })

    return render(request, 'finance/budget_tracking.html', {'budget_data': budget_data})


def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()

    return render(request, 'finance/add_budget.html', {'form': form})

def budget_list(request):
    budgets = Budget.objects.all()
    return render(request, 'finance/budget_list.html', {'budgets': budgets})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = CategoryForm()
    
    return render(request, 'finance/add_category.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'finance/category_list.html', {'categories': categories})

def add_transaction(request):
    categories = Category.objects.all()

    if not categories.exists():
        return render(request, 'finance/no_categories.html')

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'finance/add_transaction.html', {'form': form})

def testing(request):
  mydata = Transaction.objects.filter(type = 'income').values_list('amount')
  #template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  #return HttpResponse(template.render(context, request))
  return render(request, 'finance/transaction_list.html', {'transactions': mydata})


def yearly_list(request, year):
  mydata = Transaction.objects.filter(date__regex=r'^'+year).all().order_by('-date')
  total = 0
  negative = False
  income = Transaction.objects.filter(type = 'income', date__regex=r'^'+year).values_list('amount')
  if len(income) != 0:
        for plus in income:
            total = total + plus[0]
  expense = Transaction.objects.filter(type = 'expense', date__regex=r'^'+year).values_list('amount')
  if len(expense) != 0:
        for minus in expense:
            total = total - minus[0]
  if total < 0:
        total = -total
        negative = True
  return render(request, 'finance/transaction_list.html', {'transactions': mydata, 'total': total, 'negative': negative})

def monthly_list(request, year, month):
  mydata = Transaction.objects.filter(date__regex=r'^'+year+'[-]'+month).all().order_by('-date')
  total = 0
  negative = False
  income = Transaction.objects.filter(type = 'income', date__regex=r'^'+year+'[-]'+month).values_list('amount')
  if len(income) != 0:
        for plus in income:
            total = total + plus[0]
  expense = Transaction.objects.filter(type = 'expense', date__regex=r'^'+year+'[-]'+month).values_list('amount')
  if len(expense) != 0:
        for minus in expense:
            total = total - minus[0]
  if total < 0:
        total = -total
        negative = True
  return render(request, 'finance/transaction_list.html', {'transactions': mydata, 'total': total, 'negative': negative})
      
def daily_list(request, year, month, day):
  mydata = Transaction.objects.filter(date__regex=r'^'+year+'[-]'+month+'[-]'+day).all().order_by('-date')
  total = 0
  negative = False
  income = Transaction.objects.filter(type = 'income', date__regex=r'^'+year+'[-]'+month+'[-]'+day).values_list('amount')
  if len(income) != 0:
        for plus in income:
            total = total + plus[0]
  expense = Transaction.objects.filter(type = 'expense', date__regex=r'^'+year+'[-]'+month+'[-]'+day).values_list('amount')
  if len(expense) != 0:
        for minus in expense:
            total = total - minus[0]
  if total < 0:
        total = -total
        negative = True
  return render(request, 'finance/transaction_list.html', {'transactions': mydata, 'total': total, 'negative': negative})

def transaction_list(request):
    total = 0
    negative = False
    transactions = Transaction.objects.all().order_by('-date')
    income = Transaction.objects.filter(type = 'income').values_list('amount')
    if len(income) != 0:
        for plus in income:
            total = total + plus[0]
    expense = Transaction.objects.filter(type = 'expense').values_list('amount')
    if len(expense) != 0:
        for minus in expense:
            total = total - minus[0]
    if total < 0:
        total = -total
        negative = True
    return render(request, 'finance/transaction_list.html', {'transactions': transactions, 'total': total, 'negative': negative})

def front_page(request):
    return render(request, 'finance/front_page.html')
