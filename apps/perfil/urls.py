from django.urls import path
from .views import PerfilView, CambiarContraseñaView

app_name = 'apps.perfil'

urlpatterns = [
    path(
        route="",
        view=PerfilView.as_view(),
        name="perfil"
    ),

    path(
        route="cambiar-contraseña/",
        view=CambiarContraseñaView.as_view(),
        name="cambiar_contraseña"
    ),

]
