from django.db import models

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=50)
#     phone = models.CharField(max_length=10)
#     email = models.EmailField()
#     password = models.CharField(max_length=20)
#     date_join = models.DateField(auto_now_add=True)
    
#     def __str__(self):
#         return str(self.id)


# class Subscription(models.Model):
#     subs_type = models.PositiveSmallIntegerField()
#     storage_used = models.PositiveSmallIntegerField()
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return (str(self.subs_type) + "_" + str(self.user_id))

# class Files(models.Model):
#     file = models.FileField()
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
