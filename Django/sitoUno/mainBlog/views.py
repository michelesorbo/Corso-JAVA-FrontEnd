from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
#Importo il DataBase POST
from .models import Post

# Create your views here.
def index(request):
    #return HttpResponse("Ciao Mondo!!!")
    posts = Post.objects.all() #Vai nella tabella Post e selezionami tutti i post Faccio un fetchAssociativo
    #print(posts[0].titolo)
    return render(request, 'index.html', {"posts": posts})

#Ricevo dalla pagina il parametro post_id che servirà per selezionare l'articolo singolo
def post_singolo(request, post_id):
    try:
        post = Post.objects.get(pk=post_id) #Faccio una selezione sulla tabella per estrarre solo l'articolo richiesto
        return render(request, 'post.html', {'post':post})
    except:
        return redirect('index')

def michele(request):
    prof = "Mario Rossi"
    tutor = "Carlo Bianchi"
    alunni = ["Alessio","Enza","Stefania","Mohamed","Manuel"] #Scopo della lezione di domani prendere i dati dal file model
    return render(request,'michele.html', {"prof_classe":prof, "tutor_classe":tutor,"alunni":alunni})

def contatti(request):
    return render(request, 'contatti.html')