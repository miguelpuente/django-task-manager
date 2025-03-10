from django.core.validators import RegexValidator
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    telefono = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        # formato válido (+5491123456789).
        validators=[RegexValidator(r'^\+?\d{9,15}$', message="Número inválido")],
    )
    direccion = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="perfiles/", blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    def get_absolute_url(self):
        return reverse("perfil_detalle", kwargs={"pk": self.pk})
