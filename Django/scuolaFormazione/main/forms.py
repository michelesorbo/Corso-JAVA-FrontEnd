from django import forms
from .models import Alunni

class AlunniForm(forms.ModelForm):
    class Meta:
        model = Alunni
        fields = ['nome','cognome','email','tel','corso']