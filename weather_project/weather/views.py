from django.shortcuts import render

from django.conf import settings
import datetime
import requests
from weather.comms import llamar_api

# Create your views here.
# from django.http import HttpResponse

def hola_mundo(request):
    #context = {"nombre":"Beatriz",                "coches":["MERCEDES","OPEL","RENAULT","NISSAN"],                "modo_debug": False}

    context = {"nombre":"Beatriz",
               "usuarios":["Paco","Luisa","Alex75","Alicia10"],
               "contrasenas":["Pacopw","LuisaPw","Alex75Pw","Alicia10Pw"],
               "modo_debug": True}
    #return HttpResponse("<h1>hello world again</h1>")
    return render(request, "vista_tiempo.html", context)

def cargarperritos(request):
    #context = {"nombre":"Beatriz",                "coches":["MERCEDES","OPEL","RENAULT","NISSAN"],                "modo_debug": False}

    context = {"nombre":"Beatriz",
               "usuarios":["Paco","Luisa","Alex75","Alicia10"],
               "contrasenas":["Pacopw","LuisaPw","Alex75Pw","Alicia10Pw"],
               "modo_debug": True}
    #return HttpResponse("<h1>hello world again</h1>")
    return render(request, "vista_tiempo.html", context)

def widget_tiempo(request):
    #api_key = settings.KEY
    ciudad = "Galicia"
    #url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad.upper()}&appid={api_key}&units=metric"
    #respuesta = requests.get(url)
    respuesta = llamar_api(ciudad)
    data = respuesta.json()
    if respuesta.status_code == 200:
     context = {
        #"api_key" : api_key,
        "location":data["name"],
        "temperature": f"{data['main']['temp']} ºC",
        "condicition": f"{data['weather'][0]['description']}",
        "date": datetime.datetime.now()}
    #return HttpResponse("<h1>hello world again</h1>")
    else:
        context = {
        "location":"NA",
        "temperature": "NA",
        "date": datetime.datetime.now()}
    return render(request, "vista_tiempo.html", context)


"""
    #context = {"nombre":"Beatriz",                "coches":["MERCEDES","OPEL","RENAULT","NISSAN"],                "modo_debug": False}
    context = {
        "api_key" : api_key,
        "location":"Madrid",
               "temperature":"20ºC",
               "condition": "nublado",
               "date": datetime.datetime.now()}
    #return HttpResponse("<h1>hello world again</h1>")
    return render(request, "vista_tiempo.html", context) 
    """