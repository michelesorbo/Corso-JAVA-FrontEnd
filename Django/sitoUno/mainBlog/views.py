from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Ciao Mondo!!!")
    return render(request, 'index.html')

def michele(request):
    prof = "Mario Rossi"
    tutor = "Carlo Bianchi"
    alunni = ["Alessio","Enza","Stefania","Mohamed","Manuel"] #Scopo della lezione di domani prendere i dati dal file model
    return render(request,'michele.html', {"prof_classe":prof, "tutor_classe":tutor,"alunni":alunni})

def contatti(request):
    return render(request, 'contatti.html')