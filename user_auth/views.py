from pickletools import read_uint1
from django.shortcuts import get_object_or_404, render, redirect
from .forms import NewUser
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html', {})

def signup(request):
    if request.method =='POST':
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration Successful')
            return redirect("/login")
        messages.error(request, "Invalid Information")
    
    form = NewUser()
    context = {
        'form':form
    }
    return render(request, 'registration/signup.html', context)

def dashboard(request, id=id):
    user = get_object_or_404(User, id=id)
    context ={
        "first_name": user.first_name
    }
    return render(request, 'dashboard.html', context)

def account(request, id=id):
    user = get_object_or_404(User, id=id)
    context = {
        'user' : user
    }
    return render(request, 'account.html', context)