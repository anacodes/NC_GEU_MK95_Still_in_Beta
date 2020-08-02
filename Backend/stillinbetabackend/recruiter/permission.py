from rest_framework import permissions
from . import models


class IsRecruiter(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_recruiter


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsSameCompany(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.company == models.Recruiter.objects.get(user=request.user)


class IsActive(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return not obj.activate


class IsStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return not obj.status