from rest_framework import viewsets, mixins

from api.models import Appointment
from api.mixin import HospitalGenericViewSet
from api.serializers import AppointmentListSerializer, AppointmentRetrieveSerializer, AppointmentCreateSerializer, \
    AppointmentUpdateSerializer


class AppointmentView(
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
            self.action_permissions = ['view_appointment', ]
        elif self.action == 'create':
            self.action_permissions = ['add_appointment', ]
        elif self.action == 'update':
            self.action_permissions = ['change_appointment', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_appointment', ]


    def get_serializer_class(self):
        if self.action == 'list':
            return AppointmentListSerializer
        if self.action == 'retrieve':
            return AppointmentRetrieveSerializer
        if self.action == 'create':
            return AppointmentCreateSerializer
        if self.action == 'update':
            return AppointmentUpdateSerializer


    def get_queryset(self):
        return Appointment.objects.all()