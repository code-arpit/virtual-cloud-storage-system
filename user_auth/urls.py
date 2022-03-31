from django.urls import path, include

from .views import dashboard, home, signup

urlpatterns = [
    path('', home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('dashboard/<int:id>', dashboard, name='dashboard'),


]