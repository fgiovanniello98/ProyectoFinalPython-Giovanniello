from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView

from .forms import MensajeFormulario
from .models import Mensaje

class BandejaEntradaView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = "mensajeria/inbox.html"
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user)

class EnviadosView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = "mensajeria/enviados.html"
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensaje.objects.filter(remitente=self.request.user)

class MensajeDetalleView(LoginRequiredMixin, DetailView):
    model = Mensaje
    template_name = "mensajeria/detalle.html"
    context_object_name = "mensaje"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.destinatario != self.request.user and obj.remitente != self.request.user:
            raise Http404("No tenés permisos para ver este mensaje.")
        return obj

class MensajeCrearView(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = MensajeFormulario
    template_name = "mensajeria/nuevo.html"
    success_url = reverse_lazy("mensajeria:inbox")

    def get_form_kwargs(self):
        kw = super().get_form_kwargs()
        kw["usuario_actual"] = self.request.user
        return kw

    def form_valid(self, form):
        form.instance.remitente = self.request.user
        messages.success(self.request, "Mensaje enviado.")
        return super().form_valid(form)

@login_required
@require_POST
def marcar_como_leido(request, pk: int):
    '''
    View común con decorador @login_required (requisito del proyecto).
    Marca como leído un mensaje recibido.
    '''
    mensaje = get_object_or_404(Mensaje, pk=pk, destinatario=request.user)
    mensaje.leido = True
    mensaje.save(update_fields=["leido"])
    messages.success(request, "Mensaje marcado como leído.")
    return redirect("mensajeria:detalle", pk=pk)
