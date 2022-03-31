from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class Person(AbstractUser):
#     username = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=50)


# class PeronManager(models.Model):
#     user = models.OneToOneField(Person, on_delete=models.CASCADE)