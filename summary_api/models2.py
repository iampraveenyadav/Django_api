from django.db import models

 #Create your models here.
class city(models.Model):
    name=models.CharField(max_length=100)
    country_code=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    population=models.IntegerField()

  