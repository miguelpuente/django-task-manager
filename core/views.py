from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from apps.perfil.tasks import enviar_correo_reset_password

class HomeView(TemplateView):
    template_name = "base.html"


class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/registro.html"
    success_url = reverse_lazy("login")


class CustomPasswordResetView(PasswordResetView):
    email_template_name = "registration/password_reset_email.html"
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Simular que el email se envió, incluso si el usuario no existe
        email = form.cleaned_data["email"]
        subject = "Recuperación de contraseña"
        message = "Si tu email está registrado, recibirás un enlace para recuperar tu contraseña."

        # Enviar el email con Celery
        enviar_correo_reset_password.delay(email, subject, message)
        return response
