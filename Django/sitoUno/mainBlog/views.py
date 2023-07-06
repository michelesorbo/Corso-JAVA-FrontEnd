from django.shortcuts import render
from django.http import HttpResponse #Vado a importare il metodo HttpResponse di Django

# Create your views here.
def index(request):
    return HttpResponse("Benvenuto nella mia pagina.")

def mohamed(request):
    return HttpResponse("<h1>Pagina di Mohamed</h1>")