from rest_framework import viewsets, mixins

from api.models import Schedule
from api.mixin import HospitalGenericViewSet
from api.serializers import ScheduleRetrieveSerializer, ScheduleListSerializer, ScheduleCreateSerializer, ScheduleUpdateSerializer
class ScheduleView(HospitalGenericViewSet,
                   viewsets.GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):

    def get_action_permissions(self):
        if self.action == 'create':
            self.action_permissions = ['add_schedule', ]
        elif self.action == 'update':
            self.action_permissions = ['change_schedule', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_schedule', ]


    def get_serializer_class(self):
        if self.action == 'list':
            return ScheduleListSerializer
        elif self.action == 'retrieve':
            return ScheduleRetrieveSerializer
        elif self.action == 'create':
            return ScheduleCreateSerializer
        elif self.action == 'update':
            return ScheduleUpdateSerializer


    def get_queryset(self):
        return Schedule.objects.all()