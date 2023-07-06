from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Ciao Mondo!!!")
    return render(request, 'base.html')

def michele(request):
    return render(request,'michele.html')