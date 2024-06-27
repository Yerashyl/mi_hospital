from django.contrib.auth.models import Permission
from rest_framework import permissions

class RoleBasedPermissionsMixin:
    action_permissions = None

    def get_action_permissions(self):
        self.action_permissions = None

    def get_permissions(self):
        self.get_action_permissions()
        return super().get_permissions()

class HasPermissionByAuthenticatedUserRole(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if not view.action_permissions:
                return True
            for permission in view.action_permissions:
                if has_perm(permission, request.user):
                    return True
        return False

def has_perm(permission, user):
    return user.is_active and permission in get_user_permissions(user)

def get_user_permissions(user):
    if user.is_superuser:
        return set(Permission.objects.values_list('codename', flat=True))
    return set(user.user_permissions.values_list('codename', flat=True)).union(
        set(Permission.objects.filter(group__user=user).values_list('codename', flat=True))
    )
