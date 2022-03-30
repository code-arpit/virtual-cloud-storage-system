from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .forms import RegistrationForm


# Create your views here.
def home(request):
    return render(request,"home.html")


class sign_up(CreateView):
    template_name = 'registration/sign_up.html'
    form_class = RegistrationForm
    success_url = '../login/'

    def form_valid(self, form):
        # print(form.cleaned_data())
        return super().form_valid(form)