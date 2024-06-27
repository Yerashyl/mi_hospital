from rest_framework import serializers
from api.models import Service

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