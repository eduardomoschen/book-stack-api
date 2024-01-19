from rest_framework import permissions


class UserAdminPermissionClass(permissions.BasePermission):
    """
    Classe de permissão personalizada para verificar se o usuário autenticado
    tem permissão.

    Atributos:
        - Não há atributos nesta classe.

    Métodos:
        - has_permission: Determina se o usuário autenticado tem permissão para
        realizar a ação.
    """

    def has_permission(self, request, view):
        """
        Verifica se o usuário autenticado tem permissão para realizar a ação,
        e esse usuário deverá ser membro staff.

        Parâmetros:
            - request: O objeto da solicitação HTTP.
            - view: Instância da view associada à solicitação.

        Retorna:
            - True se o usuário for um membro staff.
            - False caso o contrário.
        """

        return request.user.is_staff


class UserOwnerOrAdminPermissionClass(permissions.BasePermission):
    """
    Classe de permissão personalizada para verificar se o usuário autenticado é
    proprietário da conta ou membro staff.

    Atributos:
        - Não há atributos nesta classe.

    Métodos:
        - has_object_permission: Determina se o usuário autenticado é o
        proprietário da conta ou se é um membro staff.
    """

    def has_object_permission(self, request, view, obj):
        """
        Determina se o usuário autenticado é o proprietário da conta ou se é um
        membro staff.

        Parâmetros:
            - request: O objeto da solicitação HTTP.
            - view: Instância da view associada à solicitação.

        Retorna:
            - True se o usuário autenticado for um membro staff ou se for dono
            da conta.
            - False caso contrário.
        """

        return request.user == obj or request.user.is_staff
