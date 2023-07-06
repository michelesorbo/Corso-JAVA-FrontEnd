from django.urls import path
from . import views #Vado ad importare tutte i metodi presenti nel file view.py dell'app

#Prima di creare una nuova url ricordati di creare il metodo che viene chiamata dalla nuova url
urlpatterns = [
    path('', views.index, name='index'),
    path('michele/', views.michele, name='michele'),
    path('contatti/', views.contatti, name='contatti'),
]
