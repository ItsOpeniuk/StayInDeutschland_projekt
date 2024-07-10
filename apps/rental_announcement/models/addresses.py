from django.db import models

from apps.rental_announcement.choices.federal_lands import FederalLands

class ObjectAddress(models.Model):
    federal_land = models.CharField(max_length=50, choices=FederalLands.choices)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=75)
    house_number = models.CharField(max_length=5)
    postal_code = models.CharField(max_length=5)