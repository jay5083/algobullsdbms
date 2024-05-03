from django.urls import path, include
from .views import home

urlpatterns = [
    path('accounts/profile/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
