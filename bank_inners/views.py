from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import *
from .models import *
from .decorators import *

@login_required(login_url='loginPage')
def home(request):
    current_user = request.user
    account_balance = get_object_or_404(UserProfile, user=current_user)
    context = {'account_balance':account_balance}
    return render(request, 'bank_inners/dashboard.html', context)

def analytics(request):
    return render(request, 'bank_inners/analytics.html')

@login_required(login_url='loginPage')
def profile(request):
    return render(request, 'bank_inners/profile.html')

@login_required(login_url='loginPage')
def deposit(request):
    return render(request, 'bank_inners/deposit.html')

@unauthenticated_user
def reg(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Your Account has been created successfully! '+ user)

            return redirect('loginPage')

    context = {'form':form}
    return render(request, 'bank_inners/reg.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'bank_inners/loginPage.html', context)

@login_required(login_url='loginPage')
def LogoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required(login_url='loginPage')
def reports(request):
    return render(request, 'bank_inners/reports.html')

@login_required(login_url='loginPage')
def settings(request):
    return render(request, 'bank_inners/settings.html')

@login_required(login_url='loginPage')
def support_agent(request):
    return render(request, 'bank_inners/support_agent.html')

@login_required(login_url='loginPage')
def withdraw(request):
    return render(request, 'bank_inners/withdrawal.html')
