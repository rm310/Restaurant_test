from django.db.models.signals import post_save
from django.dispatch import receiver
from restaurant.models import DishesMenu

@receiver(post_save, sender=DishesMenu)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        print("Malumot qoshildi")