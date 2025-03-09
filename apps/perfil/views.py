from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View

class LoginView(View):
    template_name = "usuarios/login.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get("login-user")
        password = request.POST.get("login-pass")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")  # Redirige al home
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            return render(request, self.template_name)


# Register View (View)
class RegisterView(View):
    template_name = "usuarios/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("signup-user")
        email = request.POST.get("signup-email")
        password = request.POST.get("signup-pass")
        password2 = request.POST.get("signup-repeat-pass")

        # Validaciones
        if password != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, self.template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, self.template_name)

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está en uso.")
            return render(request, self.template_name)

        # Crear usuario
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Iniciar sesión automáticamente
        login(request, user)
        return redirect("home")  # Redirigir al dashboard tras el registro

# 🔹 Logout View
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("auth:login")