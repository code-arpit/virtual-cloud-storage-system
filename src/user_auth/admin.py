from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Subscription, Files

# Register your models here.

admin.site.register(Subscription)
admin.site.register(Files)