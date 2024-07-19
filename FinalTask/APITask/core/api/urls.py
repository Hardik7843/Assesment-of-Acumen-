from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.show),
    path('add' , views.add),
    path('csv' , views.add_csv),
    path('company' , views.add_companies)
]