from rest_framework import permissions



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to view it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for all users
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed for the owner of the snippet
        return obj.owner == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit objects.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

class IsActiveOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow active users to view objects.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_active

class IsSuperUser(permissions.BasePermission):
    """
    Custom permission to only allow superusers to view objects.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser



