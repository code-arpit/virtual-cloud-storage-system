from django.shortcuts import render, redirect
from .forms import NewUser
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def signup(request):
    if request.method =='POST':
        form = NewUser(request.POST)
        print(form)
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


# <label for="form.username"><b>Username</b></label>
#               {{ form.username }}<br>
#               <label for="form.email"><b>Enter Email</b></label> <br>
#               {{ form.email }}<br>
         
#               <label for="form.password1"><b>Enter Password</b></label> <br>
#               {{ form.password1 }}<br>
#               <label for="form.password2"><b>Re-Enter Password</b></label> <br>
#               {{ form.password2 }}<br>