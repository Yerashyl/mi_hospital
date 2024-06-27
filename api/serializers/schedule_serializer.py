from rest_framework import serializers
from api.models import Schedule, Patient, Doctor, Appointment

class ScheduleListSerializer(serializers.Serializer):
    Doctor.full_name = serializers.CharField()
    Patient.full_name = serializers.CharField()
    Appointment.date_time = serializers.DateTimeField()

class ScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ScheduleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['appointment', ]

class ScheduleRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'