from rest_framework import serializers
from api.models import FinancialMetrics

class FinancialMetricsListSerializer(serializers.Serializer):
    profit = serializers.DecimalField(max_digits=10, decimal_places=2)

class FinancialMetricsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialMetrics
        fields = ['income', 'expenses']

class FinancialMetricsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialMetrics
        fields = ['income', 'expenses']

class FinancialMetricsRetrieveSerializer(serializers.ModelSerializer):
    profit = serializers.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = FinancialMetrics
        fields = '__all__'