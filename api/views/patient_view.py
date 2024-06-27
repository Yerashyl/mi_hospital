from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins

from api.models import Patient
from api.filters import PatientFilterSet
from api.mixin import HospitalGenericViewSet
from api.serializers import PatientListSerializer, PatientRetrieveSerializer, PatientCreateSerializer, \
    PatientUpdateSerializer


class PatientView(
    HospitalGenericViewSet,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('first_name', 'last_name', 'age', 'gender', )
    filterset_class = PatientFilterSet

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_patient', ]
        elif self.action == 'create':
            self.action_permissions = ['add_patient', ]
        elif self.action == 'update':
            self.action_permissions = ['change_patient', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_patient', ]

    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        if self.action == 'retrieve':
            return PatientRetrieveSerializer
        if self.action == 'create':
            return PatientCreateSerializer
        if self.action == 'update':
            return PatientUpdateSerializer

    def get_queryset(self):
        return Patient.objects.all()
