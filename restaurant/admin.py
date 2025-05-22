from django.contrib import admin
from restaurant.models import DishesMenu, ContactInfo, BookingPlace, Orders

@admin.register(DishesMenu)
class DishesMenuAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(BookingPlace)
class BookingPlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    pass

