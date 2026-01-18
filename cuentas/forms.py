from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Perfil

Usuario = get_user_model()

class RegistroUsuarioFormulario(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ("username", "email", "password1", "password2")

class UsuarioActualizarFormulario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ("first_name", "last_name", "email")

class PerfilActualizarFormulario(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ("avatar", "biografia", "fecha_nacimiento")
        widgets = {
            "biografia": forms.Textarea(attrs={"rows": 4, "placeholder": "Contá un poquito sobre vos..."})
        }
