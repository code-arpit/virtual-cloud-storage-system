from cProfile import label
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

class SubscriptionForm(forms.Form):
    subscription_choices = [
        ('Free_plan','Free plan'),
        ('Student_plam', 'Student Plan'),
        ('Organisation_Plan', 'Organisation Plan')
    ]
    subscription_plan = forms.CharField(
        label="Choose a Subscription Plan",
        widget=forms.RadioSelect(choices=subscription_choices
        )
    )
    username = forms.CharField(max_length=50)
    
