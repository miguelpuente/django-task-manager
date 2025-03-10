from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Perfil


class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["image"]

class CambiarContraseñaForm(PasswordChangeForm):
    pass