from django.contrib import admin
from django.urls import path, include
from App.views import SigSocial
from . import views

from allauth.socialaccount.views import login_error, signup, connections, login_cancelled


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path("login/error/", login_error, name="socialaccount_login_error"),
    path("signup/", signup, name="socialaccount_signup"),
    path("connections/", connections, name="socialaccount_connections"),
    path(
        "login/cancelled/",
        login_cancelled,
        name="socialaccount_login_cancelled",
    ),
    path('', views.home, name='home'),
    path("SignupSocial/", SigSocial.as_view(), name="socialaccount_signup"),

]

