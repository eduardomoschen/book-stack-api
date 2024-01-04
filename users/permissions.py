from rest_framework import permissions


class UserAdminPermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        """
        Aqui é onde o admin tem permissão.
        """
        return request.user.is_staff


class UserOwnerOrAdminPermissionClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        User ou admin tem acesso
        """
        return request.user == obj or request.user.is_staff