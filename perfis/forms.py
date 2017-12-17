
from django import forms

class pesquisar(forms.Form):
    texto=forms.CharField(required=False)