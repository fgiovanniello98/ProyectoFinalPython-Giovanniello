from django import forms
from .models import Pagina

class PaginaFormulario(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ["titulo", "subtitulo", "contenido", "imagen"]
        widgets = {
            "titulo": forms.TextInput(attrs={"placeholder": "Ej: Mi primera página"}),
            "subtitulo": forms.TextInput(attrs={"placeholder": "Un resumen cortito para el listado..."}),
        }
