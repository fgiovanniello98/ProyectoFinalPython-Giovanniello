from django.contrib import messages
from django.contrib.auth import views as vistas_auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import RegistroUsuarioFormulario, UsuarioActualizarFormulario, PerfilActualizarFormulario

class RegistroView(SuccessMessageMixin, CreateView):
    template_name = "cuentas/registro.html"
    form_class = RegistroUsuarioFormulario
    success_url = reverse_lazy("cuentas:login")
    success_message = "Cuenta creada. Ahora podés iniciar sesión."

class LoginView(vistas_auth.LoginView):
    template_name = "cuentas/login.html"

class LogoutView(vistas_auth.LogoutView):
    pass

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = "cuentas/perfil.html"

class PerfilEditarView(LoginRequiredMixin, UpdateView):
    template_name = "cuentas/editar_perfil.html"
    form_class = PerfilActualizarFormulario
    success_url = reverse_lazy("cuentas:perfil")

    def get_object(self, queryset=None):
        return self.request.user.perfil

    def form_valid(self, form):
        messages.success(self.request, "Perfil actualizado.")
        return super().form_valid(form)

def editar_datos_usuario(request):
    if not request.user.is_authenticated:
        return redirect("cuentas:login")

    if request.method == "POST":
        formulario = UsuarioActualizarFormulario(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Datos del usuario actualizados.")
            return redirect("cuentas:perfil")
    else:
        formulario = UsuarioActualizarFormulario(instance=request.user)

    return render(request, "cuentas/editar_usuario.html", {"formulario": formulario})

class CambiarPasswordView(LoginRequiredMixin, vistas_auth.PasswordChangeView):
    template_name = "cuentas/cambiar_password.html"
    success_url = reverse_lazy("cuentas:perfil")

    def form_valid(self, form):
        messages.success(self.request, "Contraseña cambiada con éxito.")
        return super().form_valid(form)
