from django.db import models

# create models for restaurant apis
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
class Menu(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2)
