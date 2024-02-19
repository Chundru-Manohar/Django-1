from django.shortcuts import render
import urllib
import json
# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST.get('city')
        url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=b5baa31b0916a50f86faadbe2c39bad3').read()
        api_url2 =json.loads(url)
        
        data = {
            'city': city,
            'weather_d':api_url2['weather'][0]['description'],
            'weather_t':api_url2['main']['temp'],
            'weather_p':api_url2['main']['pressure'],
            'weather_h':api_url2['main']['humidity'],
            'weather_i':api_url2['weather'][0]['icon'],
            'weather_s':api_url2['sys']['sunrise'],
            'weather_ss':api_url2['sys']['sunset']
        }
    else:
        data = {
        'city': None,
        'weather_d':None,
        'weather_t':None,
        'weather_p':None,
        'weather_h':None,
        'weather_i':None,
        }

    return render(request,'index.html',{'data':data})