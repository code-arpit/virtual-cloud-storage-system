import os

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FileForm, NewUser, SubscriptionForm
from .models import Files, Subscription


def home(request):
    return render(request, "home.html", {})


def signup(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            username = request.POST.get("username")

            form.save()
            messages.success(request, "Registration Successful")
            return redirect(
                f"/subscription/{username}",
            )
        messages.error(request, "Invalid Information")

    form = NewUser()
    context = {"form": form}
    return render(request, "registration/signup.html", context)


def subscription(request, id=id):
    username = id
    if request.method == "POST":
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            form_subs = form.cleaned_data["subscription_plan"]

            form_data = Subscription(subscription_plan=form_subs, username=username)
            form_data.save()
            return redirect("/login")

    form = Subscription()
    context = {"username": username, "subscription_plan": form.subscription_plan}
    return render(request, "subscription.html", context)


def dashboard(request, id=id):
    context = {}
    user = get_object_or_404(User, username=id)
    files = Files.objects.filter(username=id)

    if request.method == "POST":

        form = FileForm(request.FILES)
        upload = request.FILES["file"]
        object = Files.objects.create(username=id, upload=upload)
        object.save()
        file_message = messages.success(request, "File Upload Successfully")
        context.update({"message": file_message})

    form = FileForm()
    context.update(
        {
            "files": files,
            "upload_form": form,
            "first_name": user.first_name,
        }
    )

    return render(request, "dashboard.html", context)


def plan_info(plan):
    plan_information = []
    if plan == "Student_Plan":
        plan_information.append("Student Plan")
        plan_information.append(10)
        return plan_information
    elif plan == "Organisation_Plan":
        plan_information.append("Organisation Plan")
        plan_information.append(25)
        return plan_information
    else:
        plan_information.append("Free Plan")
        plan_information.append(5)
        return plan_information


def account(request, id=id):
    user = User.objects.get(username=id)
    storage = Subscription.objects.get(username=id)
    plan = plan_info(storage.subscription_plan)
    selected_plan = plan[0]

    memory = 0
    files = Files.objects.filter(username=id)
    if files:
        for file in files:
            size = file.get_size()[0]
            memory = memory + size

    storage_used = memory
    print(storage_used)
    allocated_storage = plan[1]
    print(allocated_storage)
    remaining_storage = round((allocated_storage - (storage_used / 1000)), 4)
    print(remaining_storage)
    context = {
        "user": user,
        "selected_plan": selected_plan,
        "allocated_storage": allocated_storage,
        "remaining_storage": remaining_storage,
    }
    return render(request, "account.html", context)
