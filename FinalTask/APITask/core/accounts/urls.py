from django.urls import re_path

from . import views

urlpatterns = [
    re_path('signup', views.signup),
    re_path('login_req', views.login_req),
    re_path('login', views.login),
]