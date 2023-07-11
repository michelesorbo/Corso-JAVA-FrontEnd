from django.shortcuts import render, redirect
from .models import Corsi
from .forms import AlunniForm

# Create your views here.
def index(require):
    return render(require,'main/index.html')

def CorsiView(require):
    corsi = Corsi.objects.all()
    return render(require, 'corsi/corsi.html', {"corsi":corsi})

def CorsoView(require, corso_id):
    corso = Corsi.objects.get(pk = corso_id)
    return render(require,'corsi/corso.html', {"corso":corso})

def CorsiByCat(require, cat_id):
    corsi = Corsi.objects.all().filter(categoria=cat_id)
    return render(require, 'corsi/corsi.html', {"corsi":corsi})

def Candidatura(request):
    if request.method == 'POST':
        form = AlunniForm(request.POST)
        if form.is_valid():
            alunni = form.save(commit=False)
            alunni.save()
            return redirect('index')
    else:
        form = AlunniForm()
    
    return render(request,'corsi/richiesta.html', {"form":form})
            