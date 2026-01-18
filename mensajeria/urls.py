from django.urls import path
from .views import (
    BandejaEntradaView,
    EnviadosView,
    MensajeDetalleView,
    MensajeCrearView,
    marcar_como_leido,
)

app_name = "mensajeria"

urlpatterns = [
    path("", BandejaEntradaView.as_view(), name="inbox"),
    path("enviados/", EnviadosView.as_view(), name="enviados"),
    path("nuevo/", MensajeCrearView.as_view(), name="nuevo"),
    path("<int:pk>/", MensajeDetalleView.as_view(), name="detalle"),
    path("<int:pk>/leido/", marcar_como_leido, name="leido"),
]
