from .models import Menu, Booking
from rest_framework import serializers

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'