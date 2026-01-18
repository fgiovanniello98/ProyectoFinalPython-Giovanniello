from django.urls import path
from .views import (
    PaginaListadoView,
    PaginaDetalleView,
    PaginaCrearView,
    PaginaActualizarView,
    PaginaBorrarView,
)

app_name = "paginas"

urlpatterns = [
    path("", PaginaListadoView.as_view(), name="listado"),
    path("crear/", PaginaCrearView.as_view(), name="crear"),
    path("<slug:slug>/", PaginaDetalleView.as_view(), name="detalle"),
    path("<slug:slug>/editar/", PaginaActualizarView.as_view(), name="editar"),
    path("<slug:slug>/borrar/", PaginaBorrarView.as_view(), name="borrar"),
]
