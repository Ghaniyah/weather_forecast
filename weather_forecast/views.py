from django.shortcuts import render, redirect
from .forms import CityForm
from  .models import City

def index(request):
        cities = City.objects.all() #return all the cities in the database

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f6c5c870c7226d4e2d895f4c35ce00b2'
 
    ...
def index(request):
    ...
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    return render(request, 'weather/index.html') #returns the index.html template

def index(request):
    ...
    context = {'weather' : weather}

    return render(request, 'weather/index.html', context) #returns the index.html templatefor city in cities
           
city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

def index(request):
    ...
    cities = City.objects.all() #return all the cities in the database

    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

   
weather = {
         'city' :'city'
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    weather_data.append(weather) #add the data for the current city into our list

context = {'weather_data' : weather_data}



...
from .forms import CityForm

def index(request):
    ...
    form = CityForm()

    weather_data = []
    ...
    context = {'weather_data' : weather_data, 'form' : form}
    
    
    
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f6c5c870c7226d4e2d895f4c35ce00b2'

    cities = City.objects.all() #return all the cities in the database

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()
    ...

    return render(request, 'weather_forecast/index.html', context) #returns the index.html template


    
 

