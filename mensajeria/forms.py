from django import forms
from django.contrib.auth import get_user_model
from .models import Mensaje

Usuario = get_user_model()

class MensajeFormulario(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        queryset=Usuario.objects.none(),
        help_text="Elegí a quién le querés escribir."
    )

    class Meta:
        model = Mensaje
        fields = ("destinatario", "asunto", "cuerpo")
        widgets = {
            "asunto": forms.TextInput(attrs={"placeholder": "Ej: Consulta"}),
            "cuerpo": forms.Textarea(attrs={"rows": 5, "placeholder": "Escribí tu mensaje..."}),
        }

    def __init__(self, *args, **kwargs):
        usuario_actual = kwargs.pop("usuario_actual", None)
        super().__init__(*args, **kwargs)
        if usuario_actual:
            self.fields["destinatario"].queryset = Usuario.objects.exclude(id=usuario_actual.id)
        else:
            self.fields["destinatario"].queryset = Usuario.objects.all()
