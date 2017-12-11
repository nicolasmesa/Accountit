from rest_framework import permissions


def or_based(permissions):
    if type(permissions) is not list:
        raise TypeError("Expected permissions to be of type list, got {} instead".format(type(permissions)))

    def class_wrapper():
        return OrBasedPermission(permissions)

    return class_wrapper


class OrBasedPermission(permissions.BasePermission):
    """
    Custom permission that grants access if any of its passsed permissions are True
    """

    def __init__(self, permissions):
        if type(permissions) is not list:
            raise TypeError("Expected permissions to be of type list, got {} instead".format(type(permissions)))

        # Create an instance of each
        self.permissions = [Class() for Class in permissions]

    def has_permission(self, request, view):
        for permission in self.permissions:
            if permission.has_permission(request, view):
                return True

        return False

    def has_object_permission(self, request, view, obj):
        for permission in self.permissions:
            if permission.has_object_permission(request, view, obj):
                return True

        return False


class IsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_admin

    def has_permission(self, request, view):
        return request.user.is_admin


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_admin

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_admin


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user