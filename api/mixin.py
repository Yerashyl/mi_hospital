from rest_framework import viewsets

from api.permissions import RoleBasedPermissionsMixin, HasPermissionByAuthenticatedUserRole

class HospitalGenericViewSet(RoleBasedPermissionsMixin,
                             viewsets.GenericViewSet):
    permission_classes = [HasPermissionByAuthenticatedUserRole, ]