
from django.db import models
from decimal import Decimal
from django.utils import timezone


class DishesMenu(models.Model):
    dish_name = models.CharField(max_length = 20)
    description = models.TextField()
    specifications = models.CharField(max_length = 30, blank=True, default='No specifications')
    price = models.DecimalField(max_digits = 7, decimal_places=3)
    portion = models.CharField(max_length = 20)

    def __str__(self):
        return self.dish_name

class ContactInfo(models.Model):
    phone_number1 = models.CharField(max_length = 30)
    phone_number2 = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50)
    social_account1 = models.CharField(max_length = 100)
    social_account2 = models.CharField(max_length = 100)

class BookingPlace(models.Model):
    date = models.DateField()
    time = models.DateTimeField()
    place_for = models.DecimalField(max_digits=2, decimal_places=1)
    specifications = models.CharField(max_length = 20, null = True)
    phone_number = models.CharField(max_length = 30)
    customers_name = models.CharField(max_length = 20)

    class Meta:
        db_table = 'bookingplace'

class Orders(models.Model):
    orderers_name = models.CharField(max_length = 30)
    orderers_phone = models.CharField(max_length = 30)
    address = models.TextField()
    order_time = models.DateTimeField(auto_now_add = True)

    def total_price(self):
        total = sum(item.total_price() for item in self.orderdetails_set.all())
        return round(total, 2)

    def __str__(self):
        return f"Order {self.id} - {self.orderers_name}"


class OrderDetails(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    dish = models.ForeignKey(DishesMenu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return round(Decimal(self.dish.price) * self.quantity, 2)

    def __str__(self):
        return f"{self.quantity} x {self.dish.dish_name} in Order {self.order.id}"


