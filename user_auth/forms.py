from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import Person

class NewUser(UserCreationForm):
    email = forms,forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(NewUser, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class PeronForm(forms.ModelForm):
#     model = Person
#     fields = ["__all__"]


