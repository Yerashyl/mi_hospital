from rest_framework import viewsets, mixins
from api.mixin import HospitalGenericViewSet
from api.models import FinancialMetrics
from api.serializers import FinancialMetricsListSerializer, FinancialMetricsCreateSerializer, FinancialMetricsUpdateSerializer, FinancialMetricsRetrieveSerializer

class FinancialMetricsView(
    HospitalGenericViewSet,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_financialmetrics', ]
        elif self.action == 'create':
            self.action_permissions = ['add_financialmetrics', ]
        elif self.action == 'update':
            self.action_permissions = ['change_financialmetrics', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_financialmetrics', ]

    def get_serializer_class(self):
        if self.action == 'list':
            return FinancialMetricsListSerializer
        elif self.action == 'retrieve':
            return FinancialMetricsRetrieveSerializer
        elif self.action == 'update':
            return FinancialMetricsUpdateSerializer
        elif self.action == 'create':
            return FinancialMetricsCreateSerializer


    def get_queryset(self):
        return FinancialMetrics.objects.all()