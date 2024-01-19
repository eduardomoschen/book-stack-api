from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Admin para o model User.

    Métodos:
        - save_model: Sobrescreve o método para garantir que a senha do usuário
        seja criptografada ao ser salva no painel de administração.
    """

    def save_model(self, request, obj, form, change):
        """
        Salva o model de usuário no painel de administração.

        Este método garante que a senha do usuário seja criptografada ao ser
        salva no banco de dados.

        Parâmetros:
            - request: Objeto HttpRequest recebido durante a solicitação.
            - obj: Instância do model User sendo salva.
            - form: Formulário utilizado para editar o model User.
            - change: Indica se é uma atualização de um usuário existente.

        Nota:
            Se a senha for alterada ou se é uma criação de um novo usuário, a
            senha é criptografada antes de salvar.
        """

        if 'password' in form.changed_data or not change:
            raw_password = form.cleaned_data.get('password')
            obj.password = make_password(raw_password)
        super().save_model(request, obj, form, change)
