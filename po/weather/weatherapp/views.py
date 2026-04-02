from django.shortcuts import render

# Manual weather data for Indian states
WEATHER_DATA = {
    'maharashtra': {
        'city': 'Mumbai',
        'state': 'Maharashtra',
        'temperature': 28.5,
        'description': 'Partly Cloudy',
        'country': 'India',
        'humidity': 78,
        'wind_speed': 15.2
    },
    'delhi': {
        'city': 'New Delhi',
        'state': 'Delhi',
        'temperature': 32.1,
        'description': 'Clear Sky',
        'country': 'India',
        'humidity': 45,
        'wind_speed': 12.5
    },
    'karnataka': {
        'city': 'Bangalore',
        'state': 'Karnataka',
        'temperature': 26.3,
        'description': 'Rainy',
        'country': 'India',
        'humidity': 82,
        'wind_speed': 18.7
    },
    'tamil_nadu': {
        'city': 'Chennai',
        'state': 'Tamil Nadu',
        'temperature': 35.2,
        'description': 'Sunny',
        'country': 'India',
        'humidity': 65,
        'wind_speed': 22.4
    },
    'uttar_pradesh': {
        'city': 'Lucknow',
        'state': 'Uttar Pradesh',
        'temperature': 31.8,
        'description': 'Partly Cloudy',
        'country': 'India',
        'humidity': 55,
        'wind_speed': 14.3
    },
    'west_bengal': {
        'city': 'Kolkata',
        'state': 'West Bengal',
        'temperature': 29.7,
        'description': 'Humid',
        'country': 'India',
        'humidity': 85,
        'wind_speed': 16.9
    },
    'telangana': {
        'city': 'Hyderabad',
        'state': 'Telangana',
        'temperature': 34.1,
        'description': 'Clear',
        'country': 'India',
        'humidity': 48,
        'wind_speed': 11.8
    },
    'rajasthan': {
        'city': 'Jaipur',
        'state': 'Rajasthan',
        'temperature': 36.5,
        'description': 'Very Hot & Clear',
        'country': 'India',
        'humidity': 35,
        'wind_speed': 9.6
    },
    'kerala': {
        'city': 'Kochi',
        'state': 'Kerala',
        'temperature': 28.9,
        'description': 'Monsoon Showers',
        'country': 'India',
        'humidity': 90,
        'wind_speed': 25.3
    },
    'punjab': {
        'city': 'Chandigarh',
        'state': 'Punjab',
        'temperature': 30.2,
        'description': 'Partly Cloudy',
        'country': 'India',
        'humidity': 58,
        'wind_speed': 13.4
    }
}

def index(request):
    weather_data = None
    error = None
    selected_state = None
    
    if request.method == 'POST':
        state = request.POST.get('state', '').lower()
        selected_state = state
        
        if state in WEATHER_DATA:
            weather_data = WEATHER_DATA[state].copy()
        else:
            error = 'State not found. Please select from available states.'

    return render(request, 'weather/index.html', {
        'weather_data': weather_data, 
        'error': error,
        'states': WEATHER_DATA.keys(),
        'selected_state': selected_state
    })    