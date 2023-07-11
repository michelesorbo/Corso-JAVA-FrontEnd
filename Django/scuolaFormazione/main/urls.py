from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('corsi/', views.CorsiView, name='corsi'),
    path('corso/<int:corso_id>', views.CorsoView, name='corso'),
    path('corso_cat/<int:cat_id>', views.CorsiByCat, name='corsi_cat'),
    path('richiesta_corso', views.Candidatura, name='richiesta_corso'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
