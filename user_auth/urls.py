from django.urls import path, include

from .views import home, signup

urlpatterns = [
    path('', home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup')
]