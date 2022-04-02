from django.contrib import admin
from django.urls import path
from .views import (
    get_customers,
    save_customer,
    delete_customer
)

urlpatterns = [
    path('', get_customers),
    path('save_customer/', save_customer),
    path('delete_customer/<int:id>', delete_customer)
]