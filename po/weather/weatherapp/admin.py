from django.contrib import admin
from .models import Weather

# Register your models here.

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('city', 'country', 'temperature', 'description', 'humidity', 'wind_speed', 'created_at')
    list_filter = ('country', 'created_at')
    search_fields = ('city', 'country')
