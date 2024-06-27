from rest_framework import serializers
from api.models import Patient, Doctor, Appointment


class AppointmentListSerializer(serializers.Serializer):
    Patient.full_name = serializers.CharField()
    Doctor.full_name = serializers.CharField()
    prescription = serializers.CharField()

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
