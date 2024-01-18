from rest_framework import permissions


class LibraryPermissionClass(permissions.BasePermission):
    """
    Classe de permissão personalizada para verificar se o usuário autenticado
    tem permissão.

    Atributos:
        Não há atributos nesta classe.

    Métodos:
        has_permission: Determina se o usuário autenticado tem permissão para
        realizer a ação.
    """

    def has_permission(self, request, view):
        """
        Verifica se o usuário autenticado tem permissão para realizar a ação.

        Parâmetros:
            request: O objeto da solicitação HTTP.
            request: Instância da view associada à solicitação.

        Retorna:
            - True se o usuário for um membro staff para todas as
            funcionalidades e para o método POST o usuário deve estar
            autenticado.
            - False caso o contrário.
        """

        if request.user.is_staff:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        return False


class LibraryUserOwnerOrAdminPermissionClass(permissions.BasePermission):
    """
    Classe de permissão personalizada para verificar se o usuário autenticado é
    proprietário do empréstimo ou membro staff.

    Atributos:
        Não há atributos nesta classe.

    Métodos:
        has_object_permission: Determina se o usuário autenticado é o
        proprietário do empréstimo ou se é um membro staff.
    """

    def has_object_permission(self, request, view, obj):
        """
        Determina se o usuário autenticado é o proprietário do empréstimo ou se
        é um membro staff.

        Parâmetros:
            request: O objeto da solicitação HTTP.
            view: Instância da view associada à solicitação.

        Retorna:
            - True se o usuário autenticado for um membro staff ou se for dono
            do empréstimo.
            - False caso contrário.
        """

        return request.user.is_staff or obj.user == request.user