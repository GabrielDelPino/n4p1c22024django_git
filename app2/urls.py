from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('prueba2/', views.prueba2),
]