from rest_framework import permissions


class BookPermissionClass(permissions.BasePermission):
    """
    Classe de permissão personalizada para verificar se o usuário autenticado
    tem permissão.

    Métodos:
        has_permission: Determina se o usuário autenticado tem permissão para
        realizer a ação.
    """

    def has_permission(self, request, view):
        """
        Verifica se o usuário autenticado tem permissão para realizar a ação.

        Parâmetros:
            request: O objeto da solicitação HTTP.
            view: Instância da view associada à solicitação.

        Retorna:
            - True se o método da solicitação estiver entre os safes mathods ou
            se o usuário autenticado for um membro staff.
            - False caso contrário.
        """

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
