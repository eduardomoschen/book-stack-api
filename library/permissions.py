from rest_framework import permissions


class LibraryPermissionClass(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        return False


class LibraryUserOwnerOrAdminPermissionClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user