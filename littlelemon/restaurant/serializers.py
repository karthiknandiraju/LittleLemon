#define Serializer class for User model
from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import Menu, Booking

class MenuItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Menu
		fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = '__all__'


		