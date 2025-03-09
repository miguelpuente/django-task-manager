from django.urls import path
from .views import (
    LoginView, RegisterView, LogoutView
)

app_name = 'apps.perfil'

urlpatterns = [

    path(
        route='registro/', 
        view=RegisterView.as_view(),
        name='register'
    ),
    path(
        route='login/',
        view=LoginView.as_view(),
        name='login'
    ),
    path(route='logout/',
         view=LogoutView.as_view(),
         name='logout'
    ),

    # # Recuperación de contraseña
    # path(
    #     route='password_reset/',
    #     view=RecuperarPasswordView.as_view(),
    #     name='password_reset'
    # ),
    # path(
    #     route='password_reset_confirm/<uidb64>/<token>/',
    #     view=PasswordResetConfirmViewCustom.as_view(),
    #     name='password_reset_confirm'
    # ),
    # path(route='password_reset_complete/',
    #      view=PasswordResetCompleteViewCustom.as_view(),
    #      name='password_reset_complete'
    # ),

]