from rest_framework import permissions


class UserAndRoleVerification(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        return False