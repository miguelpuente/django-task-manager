from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import HomeView, RegistroView, CustomPasswordResetView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Vistas de autenticación incluidas en Django
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/password_reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    # Vista de registro personalizada
    path("accounts/registro/", RegistroView.as_view(), name="registro"),

    path('', HomeView.as_view(), name='home'),  # Ruta principal
    path('perfil/', include(('apps.perfil.urls'), namespace='perfil')),
]
