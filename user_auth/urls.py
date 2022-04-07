from django.urls import path, include

from .views import account, dashboard, home, signup, subscription

urlpatterns = [
    path('', home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('subscription/', subscription, name="subscription"),
    path('dashboard/<str:id>', dashboard, name='dashboard'),
    path('account/<str:id>', account, name="account")

    

]