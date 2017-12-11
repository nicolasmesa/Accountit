from rest_framework import permissions


class BlockPatch(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.method.lower() != 'patch'

    def has_permission(self, request, view):
        return request.method.lower() != 'patch'
