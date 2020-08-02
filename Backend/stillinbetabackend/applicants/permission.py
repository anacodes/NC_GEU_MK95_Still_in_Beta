from rest_framework import permissions


class IsApplicant(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_recruiter


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user