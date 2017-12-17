from django import forms


class notificacaoForm(forms.Form):
    areaTexto=forms.CharField(max_length=128)

    def is_valid(self):
        if not super(notificacaoForm, self).is_valid():
            return False
        return True
