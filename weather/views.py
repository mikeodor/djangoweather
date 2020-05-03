import requests
from django.shortcuts import render
from .models import City
from .forms import cityform
from django.views.generic import ListView
def index(request):

     cities = City.objects.all()
     url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=5299feb2c5b5f362a8e6a1af64696a30'
     
     if request.method=='POST':
          form=cityform(request.POST)
          if form.is_valid():
               form.save()

     else:
          form=cityform()
     weather_data=[]

     for city in cities:
        r = requests.get(url.format(city)).json()
        cityweather={
             'city':city,
             'temperature':r['main']["temp"],
             'description':r['weather'][0]['description'],
             'country':r['sys']['country'],
             "icon":r['weather'][0]['icon'],}
             
        weather_data.append(cityweather)
     context={
         'weather_data':weather_data,
         'form':form
    }
     print(weather_data)
     return render(request, 'weather/index.html',context)


