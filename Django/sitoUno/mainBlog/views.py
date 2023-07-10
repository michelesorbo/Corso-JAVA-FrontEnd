from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate #Importo le classi predefinite per fare il login e il logout
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



def sign_up(request):
    if request.method == 'POST': #Verifico se mi sono state passate delle variabili tramite POST
        form = RegistrationForm(request.POST) #Vado a prendere tutte le variabili del form di registrazione e le salvo nella variabile form
        if form.is_valid(): #Vado a controllare se il form è valido
            user = form.save()#Eseguo l'nserimento nella tabella e salvo la pk dell'utente appena creato
            login(request, user) #Faccio l'auto login dell'utente appena creato
            return redirect("index")#Lo reindirizzo su index una volta finita la registrazione
    else:
        form = RegistrationForm() #Vado a caricare i campi del form vuoti da visualizzare nel front end

    return render(request,'registration/sign_up.html', {"form":form})    
