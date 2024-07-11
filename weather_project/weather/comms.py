import requests
from django.conf import settings

def llamar_api(ciudad: str):
    api_key = settings.KEY
    #https://openweathermap.org/api/one-call-3#parameter
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad.upper()}&appid={api_key}&units=metric"
    respuesta = requests.get(url)
    return respuesta