from django import urls
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import account, dashboard, home, signup, subscription

urlpatterns = [
    path('', home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('subscription/<str:id>/', subscription, name="subscription"),
    path('dashboard/<str:id>/', dashboard, name='dashboard'),
    path('account/<str:id>/', account, name="account")
]

urlpatterns+=static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)