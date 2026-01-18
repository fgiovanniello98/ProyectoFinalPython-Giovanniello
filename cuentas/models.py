from django.conf import settings
from django.db import models

class Perfil(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="perfil")
    avatar = models.ImageField(upload_to="avatares", blank=True, null=True)
    biografia = models.TextField(blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Perfil de {self.usuario.username}"
