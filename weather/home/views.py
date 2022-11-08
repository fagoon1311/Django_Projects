from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    # city = 'Delhi'
    city = request.GET.get('city', 'Delhi')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=72e7ff9edb5765ea678a682c67320bee'
    data = requests.get(url).json()
    print(data)
    payload = {'city': data['name'], 
    'weather': data['weather'][0]['main'], 
    'icon': data['weather'][0]['icon'],
    'kelvin_temperature': data['main']['temp'], 
    'celsius_temperature': int(data['main']['temp']-273), 
    'pressure': data['main']['pressure'], 
    'humidity': data['main']['humidity'],
    'description': data['weather'][0]['description']
    }

    context = {'data': payload}
    print(context)

    return render(request, 'home.html', context)