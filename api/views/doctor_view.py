from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Doctor, Patient, Service, Appointment
from .permissions import DoctorAccessPermission, PatientAccessPermission, AppointmentAccessPermission
from .serializers import DoctorListSerializer, DoctorCreateSerializer, DoctorUpdateSerializer, DoctorRetrieveSerializer, \
    PatientListSerializer, PatientCreateSerializer, PatientUpdateSerializer, PatientRetrieveSerializer, ServiceListSerializer, ServiceCreateSerializer, ServiceUpdateSerializer, \
    ServiceRetrieveSerializer, AppointmentListSerializer, AppointmentCreateSerializer, AppointmentRetrieveSerializer, AppointmentUpdateSerializer


class DoctorView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    permission_classes = [IsAuthenticated, DoctorAccessPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer

    def get_queryset(self):
        return Doctor.objects.all()

    @action(detail=True, methods=['get'])
    def patients(self, request, pk=None):
        doctor = self.get_object()
        patients = Patient.objects.filter(doctor=doctor)
        serializer = PatientListSerializer(patients, many=True)
        return Response(serializer.data)

class PatientView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    permission_classes = [IsAuthenticated, PatientAccessPermission]
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

class ServiceView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

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

class AppointmentView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    permission_classes = [IsAuthenticated, AppointmentAccessPermission]

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

def index(request):
    return render(request, 'index.html')
