from django.shortcuts import render,redirect,get_object_or_404
from .forms import ExpenseForm,RegistrationForm
from .models import Expense
from django.db.models import Sum
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            instance = expense.save(commit=False)
            instance.user = request.user
            instance.save()
    exp_form = ExpenseForm()
    expenses = Expense.objects.filter(user=request.user)
    total_expenses = expenses.aggregate(Sum('amount'))
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    last_year_expenses = expenses.filter(date__gt= last_year)
    yearly_sum = last_year_expenses.aggregate(Sum('amount'))
    
    
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    last_month_expenses = expenses.filter(date__gt= last_month)
    monthly_sum = last_month_expenses.aggregate(Sum('amount'))
    # print(monthly_sum)


    last_week = datetime.date.today() - datetime.timedelta(days=7)
    last_week_expenses = expenses.filter(date__gt= last_week)
    weekly_sum = last_week_expenses.aggregate(Sum('amount'))
    # print(weekly_sum)
    
    day_sum = expenses.filter().values('date').order_by('date').annotate(sum=Sum('amount'))

    category_sum =expenses.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
    # print(category_sum)

    # print(yearly_sum)
    return render(request,'expense/index.html',{'exp_form':exp_form,'expenses':expenses,'total_expenses':total_expenses,'yearly_sum':yearly_sum,'weekly_sum':weekly_sum,'monthly_sum':monthly_sum,'day_sum':day_sum,'category_sum':category_sum})

def edit(request,id):
    expense = Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    if request.method == 'POST':
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'expense/edit.html',{'expense_form':expense_form})

def delete(request,id):
    if request.method == 'POST': 
        expense = get_object_or_404(Expense, id=id)
        expense.delete()
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'expense/register.html', {'form': form})