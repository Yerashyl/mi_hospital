from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Doctor, Patient
from api.filters import DoctorFilterSet
from api.mixin import HospitalGenericViewSet
from api.serializers import (
    DoctorListSerializer, DoctorCreateSerializer, DoctorUpdateSerializer, DoctorRetrieveSerializer,
    PatientListSerializer
)

class DoctorView(
    HospitalGenericViewSet,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['first_name', 'last_name', 'specialty']
    filterset_class = DoctorFilterSet

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_doctor', ]
        elif self.action == 'create':
            self.action_permissions = ['add_doctor', ]
        elif self.action == 'update':
            self.action_permissions = ['change_doctor', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_doctor', ]

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        elif self.action == 'retrieve':
            return DoctorRetrieveSerializer
        elif self.action == 'create':
            return DoctorCreateSerializer
        elif self.action == 'update':
            return DoctorUpdateSerializer

    def get_queryset(self):
        return Doctor.objects.all()

    @action(detail=True, methods=['get'])
    def patients(self, request, pk=None):
        doctor = self.get_object()
        patients = Patient.objects.filter(doctor=doctor)
        serializer = PatientListSerializer(patients, many=True)
        return Response(serializer.data)
