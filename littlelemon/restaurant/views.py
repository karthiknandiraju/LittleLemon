from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Menu
from .serializers import MenuItemSerializer, BookingSerializer
from .models import Booking
from rest_framework import viewsets

# Create your views here.
def index(request):
	return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer



