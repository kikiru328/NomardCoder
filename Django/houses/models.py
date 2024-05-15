from django.db import models

# Create your models here.

class House(models.Model):
    
    """Model Definition for Houses"""
    
    # describe data
    name = models.CharField(max_length=140) #house 이름
    price_per_night = models.PositiveIntegerField() #양수
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)