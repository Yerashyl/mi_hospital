from rest_framework import viewsets, mixins
from api.mixin import HospitalGenericViewSet
from api.models import Service
from api.serializers import ServiceListSerializer, ServiceRetrieveSerializer, ServiceCreateSerializer, \
    ServiceUpdateSerializer


class ServiceView(
    HospitalGenericViewSet,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_service', ]
        elif self.action == 'create':
            self.action_permissions = ['add_service', ]
        elif self.action == 'update':
            self.action_permissions = ['change_service', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_service', ]

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        if self.action == 'retrieve':
            return ServiceRetrieveSerializer
        if self.action == 'create':
            return ServiceCreateSerializer
        if self.action == 'update':
            return ServiceUpdateSerializer


    def get_queryset(self):
        return Service.objects.all()