from django import forms
from .models import DishesMenu, ContactInfo, BookingPlace, Orders, OrderDetails
from django.forms import modelformset_factory

class MenuPage(forms.ModelForm):
    class Meta:
        model = DishesMenu
        fields = ['dish_name', 'description', 'specifications', 'price', 'portion']

class ContactInfoPage(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['phone_number1', 'phone_number2', 'email', 'social_account1', 'social_account2']

class BookingPage(forms.ModelForm):
    class Meta:
        model = BookingPlace
        fields = ['date', 'time', 'place_for', 'specifications', 'phone_number', 'customers_name']

class OrdersPage(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['orderers_name', 'orderers_phone', 'address']


class OrderDetailsPage(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ['dish', 'quantity']


OrderDetailsFormSet = modelformset_factory(OrderDetails, form=OrderDetailsPage, extra=10)

