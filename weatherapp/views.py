from django.shortcuts import render
import requests
import datetime
# Create your views here.
def index(request):


    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Cebu'



    appid = '7828fd0a61910b92a261914b6ee796e8'
    URL = f'http://api.openweathermap.org/data/2.5/weather?'
    PARAMS ={'q':'city', 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    pressure = res['main']['pressure']
   
    humidity = res['main']['humidity']
   
    

    day = datetime.date.today()

    return render(request, 'weatherapp/index.html',{'description': description,
    'icon':icon, 'temp':temp, 'pressure':pressure,
     'humidity':humidity, 'day':day, 'city':city})