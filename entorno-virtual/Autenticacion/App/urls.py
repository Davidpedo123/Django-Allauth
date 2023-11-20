from django.contrib import admin
from django.urls import path, include
from .views import LoginApp,  profile


urlpatterns = [
    path('accounts/', include('allauth.urls')),

]

