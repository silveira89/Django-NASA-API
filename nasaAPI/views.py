from django.shortcuts import render
import requests
from decouple import config

# Create your views here.

def requestNasaAPI(request):
    # URL da API que você deseja consumir
    api_url = config('API_KEY')

    # Realize a requisição GET
    response = requests.get(api_url)

    # Verifique o código de status da resposta
    if response.status_code == 200:
        # A resposta foi bem-sucedida
        data = response.json()  # Parseie a resposta JSON
        # Agora, você pode trabalhar com os dados como desejar
        return render(request, 'nasaAPI/home.html', data)
    else:
        # A resposta não foi bem-sucedida
        return render(request, 'nasaAPI/home.html')