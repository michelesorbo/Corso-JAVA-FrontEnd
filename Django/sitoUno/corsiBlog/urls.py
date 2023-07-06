from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='corsiHome'),
    path("java", views.corsoJAVA, name='corsoJAVA'),
]
