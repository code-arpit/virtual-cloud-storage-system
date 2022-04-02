from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Subscription

class NewUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(NewUser, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class Subscription():
    class Meta:
        model = Subscription
        fields = ["__all__"]
    
    def save(self, commit=True):
        subs = super(Subscription, self).save(commit=False)
        subs = self.cleaned_data['subsription_plan']
        if commit:
            subs.save()
        return subs