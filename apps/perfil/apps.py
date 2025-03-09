from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.perfil'

    def ready(self):
        import apps.perfil.signals  # Asegura que los signals se ejecuten