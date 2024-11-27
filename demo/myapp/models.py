from django.db import models

# models are blueprint templates for DBs

# Create your models here.
class Tour(models.Model):
    # origin country, destination, num nights, price
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    price = models.IntegerField()