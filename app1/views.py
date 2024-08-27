from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html="""
    <h1>Soy el index de la app1</h1>
    <h2>hola!</h2>
    """
    return HttpResponse(html)

def prueba(request):
    html="""
    <h1 style="color:blue">Soy una prueba</h1>
    <h2 style="color:red">BENZEMAAAAAAAAAA</h2>
    """
    return HttpResponse(html)