from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from .forms import PerfilForm, CambiarContraseñaForm, ProfileImageForm
from django.contrib.auth.models import User

class PerfilView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = PerfilForm
    template_name = "registration/perfil/perfil.html"
    success_url = reverse_lazy("perfil")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["password_form"] = CambiarContraseñaForm(self.request.user)
        context["image_form"] = ProfileImageForm(instance=self.request.user.perfil)
        return context

    def post(self, request, *args, **kwargs):
        user_form = PerfilForm(request.POST, instance=request.user)
        image_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.perfil)

        if user_form.is_valid() and image_form.is_valid():
            user_form.save()
            image_form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("perfil")

        return self.get(request, *args, **kwargs)

class CambiarContraseñaView(LoginRequiredMixin, PasswordChangeView):
    form_class = CambiarContraseñaForm
    template_name = "registration/perfil/perfil.html"
    success_url = reverse_lazy("perfil:perfil")

    def form_valid(self, form):
        messages.success(self.request, "Contraseña cambiada correctamente.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al cambiar la contraseña.")
        return super().form_invalid(form)
