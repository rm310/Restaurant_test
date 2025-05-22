from rest_framework import serializers
from .models import DishesMenu

class DishesMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishesMenu
        fields = '__all__'
