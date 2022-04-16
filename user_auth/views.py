from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import NewUser, SubscriptionForm
from .models import Subscription

def home(request):
    return render(request, 'home.html', {})

def signup(request):
    if request.method =='POST':
        form = NewUser(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            print(username)
            form.save()
            messages.success(request, 'Registration Successful')
            return redirect(f"/subscription/{username}", )
        messages.error(request, "Invalid Information")
    
    form = NewUser()
    context = {
        'form':form
    }
    return render(request, 'registration/signup.html', context)

def subscription(request, id=id):
    username = id
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        # print(form)
        # form.subscription_plan = request.POST.get("subscription_plan")
        # print(form.subscription_plan)
        # print(form.cleaned_data)
        if form.is_valid():
            form_user = form.cleaned_data['username']
            form_subs = form.cleaned_data['subscription_plan']
            form_data = Subscription(subscription_plan = form_subs, username = username)
            form_data.save()
            return redirect("/login")

    form = Subscription()
    context = {
        'username' : username,
        'subscription_plan': form.subscription_plan
    }
    return render(request, "subscription.html", context)

def dashboard(request, id=id):
    user = get_object_or_404(User, username=id)
    # user = User.objects.get(username=username)

    context ={
        "first_name": user.first_name
    }
    return render(request, 'dashboard.html', context)

def plan_info(plan):
    plan_information = []
    if plan == "Student_Plan":
        plan_information.append('Student Plan')
        plan_information.append(10)
        return plan_information
    elif plan == "Organisation_Plan":
        plan_information.append('Organisation Plan')
        plan_information.append(25)
        return plan_information
    else:
        plan_information.append('Free Plan')
        plan_information.append(5)
        return plan_information

def account(request, id=id):
    user = User.objects.get(username=id)
    storage = Subscription.objects.get(username=id)
    plan = plan_info(storage.subscription_plan)
    storage_used = storage.storage_used
    # print(plan)
    selected_plan = plan[0]
    allocated_storage = plan[1]
    remaining_storage = allocated_storage - storage_used
    # print(f'--------------{remaining_storage}')

    context = {
        'user' : user,
        'allocated_storage' : allocated_storage,
        'selected_plan' : selected_plan,
        'remaining_storage' : remaining_storage
    }
    return render(request, 'account.html', context)

