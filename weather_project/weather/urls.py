
from django.urls import path
import weather.views as views

urlpatterns = [
    path("", views.widget_tiempo),
    path("\hola", views.hola_mundo),
    path("\perrito", views.cargarperritos)
]
