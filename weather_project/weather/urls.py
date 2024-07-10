
from django.urls import path
import weather.views as views

urlpatterns = [
    path("hola_mundo/", views.hola_mundo)
]
