from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Pagina(models.Model):
    titulo = models.CharField(max_length=120)
    subtitulo = models.CharField(max_length=160)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    contenido = RichTextUploadingField()
    imagen = models.ImageField(upload_to="paginas", blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="paginas")

    class Meta:
        ordering = ["-fecha_publicacion"]

    def __str__(self) -> str:
        return f"{self.titulo} — {self.autor}"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.titulo)[:150] or "pagina"
            slug = base
            contador = 1
            while Pagina.objects.filter(slug=slug).exists():
                contador += 1
                slug = f"{base}-{contador}"
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("paginas:detalle", kwargs={"slug": self.slug})
