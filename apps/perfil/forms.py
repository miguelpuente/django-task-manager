from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    telefono = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'telefono', 'password1', 'password2']
