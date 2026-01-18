from django.urls import path
from .views import (
    RegistroView, LoginView, LogoutView,
    PerfilView, PerfilEditarView, editar_datos_usuario,
    CambiarPasswordView
)

app_name = "cuentas"

urlpatterns = [
    path("registro/", RegistroView.as_view(), name="registro"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("perfil/", PerfilView.as_view(), name="perfil"),
    path("perfil/editar/", PerfilEditarView.as_view(), name="editar_perfil"),
    path("perfil/usuario/", editar_datos_usuario, name="editar_usuario"),
    path("perfil/password/", CambiarPasswordView.as_view(), name="cambiar_password"),
]
