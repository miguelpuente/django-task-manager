from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    """Crea un perfil automáticamente cuando se crea un nuevo usuario."""
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    """Guarda el perfil cada vez que se actualiza el usuario."""
    instance.perfil.save()