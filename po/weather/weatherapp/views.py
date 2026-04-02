from django.shortcuts import render
from django.http import JsonResponse
from .models import Weather


def index(request):
    cities = Weather.objects.order_by('city').values_list('city', flat=True).distinct()
    selected_city = None
    weather_data = None
    error = None

    if request.method == 'POST':
        selected_city = request.POST.get('city')
        if selected_city:
            weather_data = Weather.objects.filter(city=selected_city).first()
            if not weather_data:
                error = f"No weather record found for city: {selected_city}."
        else:
            error = "Please select a city."

    return render(request, "weather/index.html", {
        "cities": cities,
        "selected_city": selected_city,
        "weather_data": weather_data,
        "error": error,

    })
