from rest_framework import serializers
from .models import Patient, Doctor, Appointment, Service
class DoctorListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    phone = serializers.CharField()

class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['specialty', 'phone', 'schedule']


class DoctorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class PatientListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    phone = serializers.CharField()

class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['age', 'phone', 'doctor', 'medical_history']
class PatientRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class ServiceListSerializer(serializers.Serializer):
    name= serializers.CharField()
    price = serializers.IntegerField()

class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['price']


class ServiceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class AppointmentListSerializer(serializers.Serializer):
    Patient.full_name = serializers.CharField()
    Doctor.full_name = serializers.CharField()
    Prescription = serializers.CharField()

class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date_time', 'status']


class AppointmentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
