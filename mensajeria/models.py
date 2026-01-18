from django.conf import settings
from django.db import models

class Mensaje(models.Model):
    remitente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mensajes_enviados")
    destinatario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mensajes_recibidos")
    asunto = models.CharField(max_length=120)
    cuerpo = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ["-fecha_envio"]

    def __str__(self) -> str:
        return f"{self.asunto} ({self.remitente} → {self.destinatario})"
