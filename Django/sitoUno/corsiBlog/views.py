from django.shortcuts import render, redirect
from .models import Corsi

# Create your views here.
def index(request):
    corsi = Corsi.objects.all()
    return render(request, 'corsi/index.html', {"corsi": corsi})

def corso_singolo(request, corso_id):
    try:
        corso = Corsi.objects.get(pk=corso_id)
        return render(request,'corsi/corso_singolo.html', {"corso":corso})
    except:
        return redirect('corsiHome') 

def corsoJAVA(request):
    return render(request, 'corsi/java_corso.html')