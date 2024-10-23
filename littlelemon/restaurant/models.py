from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)  # Name of the person making the booking
    no_of_guests = models.IntegerField()     # Number of guests for the booking
    BookingDATE = models.DateField()         # Date of the booking
    id = models.AutoField(primary_key=True, max_length=11)  # Integer ID for the booking
    def __str__(self):
        return f"Booking for {self.name} on {self.BookingDATE}"


class Menu(models.Model):
    title = models.CharField(max_length=255)  # Title of the menu item
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the menu item
    inventory = models.IntegerField()         # Inventory count of the item
    id = models.AutoField(primary_key=True, max_length=5)
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
