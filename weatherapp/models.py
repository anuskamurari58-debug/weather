
from django.db import models

# Create your models here.

class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    description = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city}, {self.country} - {self.temperature}°C"
