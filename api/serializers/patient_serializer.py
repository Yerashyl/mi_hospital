from rest_framework import serializers
from api.models import Patient

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