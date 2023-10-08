from django.shortcuts import render
import requests
from decouple import config
import datetime
from .models import NasaJson

# Create your views here.

def requestNasaAPI(request):
    today = str(datetime.date.today())
    data = NasaJson.objects.filter(date=today)
    if (data):
        context = {
                'title': data[0].title,
                'explanation': data[0].explanation,
                'url': data[0].url
                }
        return render(request, 'nasaAPI/home.html', context)
    else:
        api_url = config('API_KEY')
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()  # Parseie a resposta JSON
            json = NasaJson(date=data['date'],
                            explanation=data['explanation'],
                            hdurl=data['hdurl'],
                            mediaType=data['media_type'],
                            serviceVersion=data['service_version'],
                            title=data['title'],
                            url=data['url'])
            json.save()
            context = {
                    'title': data['title'],
                    'explanation': data['explanation'],
                    'url': data['url']
                    }
            return render(request, 'nasaAPI/home.html', context)
        else:
            return render(request, 'nasaAPI/home.html')