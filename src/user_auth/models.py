import os

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Person(AbstractUser):
#     username = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=50)


# class PeronManager(models.Model):
#     user = models.OneToOneField(Person, on_delete=models.CASCADE)


class Subscription(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    subscription_plan = models.CharField(max_length=50, editable=True)
    storage_used = models.DecimalField(max_digits=4, decimal_places=2, default=0, editable=True)

    def __str__(self):
        return self.subscription_plan + "_" + self.username


class Files(models.Model):
    username = models.CharField(max_length=50)
    upload = models.FileField(upload_to="media", verbose_name="")

    def __str__(self):
        self.upload = str(self.upload)[6:]
        return str(self.upload)

    def get_size(self):
        file = "media/" + str(self.upload)
        size = os.path.getsize(file)
        value = round(size / 1000000, 2)
        ext = " Mb"

        return str(value) + ext
