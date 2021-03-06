import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a5385854b084295eee5ead1ce4c11749'
    city = 'Las Vegas'
    r=requests.get(url.format(city))
    print(r.text)
    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],
    }
    print(city_weather)
    return render(request,'weather.html')