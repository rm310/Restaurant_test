from django.urls import path
from .views import contactinfo, booking, orders

urlpatterns = [
    path('contactinfo/', contactinfo, name='contactinfo'),
    path('booking/', booking, name='booking'),
    path('orders/', orders, name='orders'),
]

