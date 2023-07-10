from django import forms
from django.contrib.auth.forms import UserCreationForm #Serve per creare la fomr lato front end
from django.contrib.auth.models import User #è la tabella user del db

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True) #Rendo richiesto il campo email

    #Vado a creare la visualizzazione dei campi della form
    class Meta:
        model = User #Dare quale tabella di MODEL è presa in considerazione dalla form
        fields = ['username', 'email', 'first_name', 'last_name', 'password1','password2']#Sono i campi della tabella che voglio far vedere nei form