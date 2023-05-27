from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=500)
    img = models.ImageField(upload_to='pics')
