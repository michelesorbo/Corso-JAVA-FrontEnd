from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'corsi/index.html')

def corsoJAVA(request):
    return render(request, 'corsi/java_corso.html')