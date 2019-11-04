import requests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import Form

# Create your views here.
def user_homepage(request, name="userhomepage"):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=38e4fec38e509c018629074ac1754906'
    
    if request.method == "POST":
        form = Form(request.POST)
    if form.is_valid():
        city = request.POST["city_name"]
    else:
        form = Form()
        
    r = requests.get(url.format(city)).json()
            
    city_weather = {
        'city': city,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon' :  r['weather'][0]['icon'],
    }
            
    result = {'city_weather' : city_weather}
    return render(request, 'userhomepage.html', result, {'Form': Form})
    
# def post(self, request):

    