from django.contrib.auth.mixins import UserPassesTestMixin

class UsuarioEsAutorMixin(UserPassesTestMixin):
    '''
    Mixin para asegurar que solo el autor pueda editar/borrar una página.
    Cumple el requisito de usar al menos un mixin en una CBV.
    '''
    def test_func(self):
        objeto = self.get_object()
        return objeto.autor == self.request.user
