from django.apps import AppConfig


class LibraryConfig(AppConfig):
    """
    Configuração da aplicação library.

    Atributos:
        - default_auto_field: Define o campo automático padrão para models.
        - name: Nome da aplicação.

    Métodos:
        - ready: Sobrescrito para importar os signals quando a aplicação
        estiver pronta.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'

    def ready(self):
        """
        Método chamado quando a aplicação está pronta.

        Este método é sobrescrito para importar os sinais quando a aplicação é
        carregada. Isso garante que os sinais sejam registrados e ativados
        automaticamente.
        """

        import library.signals