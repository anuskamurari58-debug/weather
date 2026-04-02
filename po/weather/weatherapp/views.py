from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    weather_data = None
    error = None
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url).json()

        if response.get('cod') == 200:
            weather_data = {
                'city': response['name'],
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'country': response['sys']['country'],
                'humidity': response['main']['humidity'],
                'wind_speed': round(response['wind']['speed'] * 3.6, 1)  # Convert m/s to km/h
            }
        else:
            error = 'City not found or API error.'

    return render(request, 'weather/index.html', {'weather_data': weather_data, 'error': error})    