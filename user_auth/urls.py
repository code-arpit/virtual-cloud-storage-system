from django.urls import path, include

from .views import home, sign_up

urlpatterns = [
    path('home/', home, name='home'),
    path('user/signup/', sign_up.as_view(), name='signup')


]