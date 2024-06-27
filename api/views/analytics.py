from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Avg

from api.mixin import HospitalGenericViewSet
from api.service import get_upcoming_appointments_count
from api.models import Doctor, Patient, Appointment, FinancialMetrics
from api.serializers import FinancialMetricsRetrieveSerializer

class AnalyticsView(HospitalGenericViewSet):
    @action(detail=False, methods=['get'])
    def get_analytics(self, request):
        patient_count = Patient.objects.count()
        doctor_count = Doctor.objects.count()
        upcoming_appointments_count = get_upcoming_appointments_count()
        average_rating = Appointment.objects.filter(status='Completed').aggregate(Avg('rating'))['rating__avg']
        patient_satisfaction = "acceptable" if average_rating and average_rating > 3.5 else "non-acceptable"
        financial_metrics = FinancialMetrics.objects.latest('id')
        financial_metrics_serializer = FinancialMetricsRetrieveSerializer(financial_metrics)

        response = {
            'patient_count': patient_count,
            'doctor_count': doctor_count,
            'upcoming_appointments_count': upcoming_appointments_count,
            'patient_satisfaction': patient_satisfaction,
            'financial_metrics': financial_metrics_serializer.data,
        }

        return Response(status=status.HTTP_200_OK, data=response)