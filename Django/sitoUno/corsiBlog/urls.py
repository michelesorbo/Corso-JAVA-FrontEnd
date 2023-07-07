from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='corsiHome'),
    path('corso/<int:corso_id>', views.corso_singolo, name='corso_singolo'),
    path("java", views.corsoJAVA, name='corsoJAVA'),
]
