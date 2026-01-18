from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Pagina
from .forms import PaginaFormulario
from .mixins import UsuarioEsAutorMixin

def vista_home(request):
    return render(request, "home.html")

def vista_about(request):
    return render(request, "about.html")

class PaginaListadoView(ListView):
    model = Pagina
    template_name = "paginas/listado.html"
    context_object_name = "paginas"
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        consulta = self.request.GET.get("q", "").strip()
        if consulta:
            qs = qs.filter(
                Q(titulo__icontains=consulta)
                | Q(subtitulo__icontains=consulta)
                | Q(contenido__icontains=consulta)
                | Q(autor__username__icontains=consulta)
            )
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["q"] = self.request.GET.get("q", "").strip()
        return ctx

class PaginaDetalleView(DetailView):
    model = Pagina
    template_name = "paginas/detalle.html"
    context_object_name = "pagina"
    slug_field = "slug"
    slug_url_kwarg = "slug"

class PaginaCrearView(LoginRequiredMixin, CreateView):
    model = Pagina
    form_class = PaginaFormulario
    template_name = "paginas/formulario.html"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, "Página creada con éxito.")
        return super().form_valid(form)

class PaginaActualizarView(LoginRequiredMixin, UsuarioEsAutorMixin, UpdateView):
    model = Pagina
    form_class = PaginaFormulario
    template_name = "paginas/formulario.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def form_valid(self, form):
        messages.success(self.request, "Página actualizada con éxito.")
        return super().form_valid(form)

class PaginaBorrarView(LoginRequiredMixin, UsuarioEsAutorMixin, DeleteView):
    model = Pagina
    template_name = "paginas/confirmar_borrado.html"
    success_url = reverse_lazy("paginas:listado")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Página borrada.")
        return super().delete(request, *args, **kwargs)
