from django.urls import path
from .views import index, DoctorView, AppointmentView, ServiceView, PatientView, ScheduleView, AnalyticsView, FinancialMetricsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('doctor/',
         DoctorView.as_view({
             'get': 'list',
             'post': 'create'
         })
    ),
    path('doctor/<int:pk>/',
         DoctorView.as_view({
             'get': 'retrieve',
             'put': 'update',
             'delete': 'destroy'
         })
    ),
    path('patient/',
         PatientView.as_view({
             'get': 'list',
             'post': 'create'
         })
         ),
    path('patient/<int:pk>/',
         PatientView.as_view({
             'get': 'retrieve',
             'put': 'update',
             'delete': 'destroy'
         })),
    path('service/',
         ServiceView.as_view({
             'get': 'list',
             'post': 'create'
         })
    ),
    path('service/<int:pk>/',
         ServiceView.as_view({
             'get': 'retrieve',
             'put': 'update',
             'delete': 'destroy'
         })
    ),
    path('appointment/', AppointmentView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('appointment/<int:pk>/',
         AppointmentView.as_view({
             'get': 'retrieve',
             'put': 'update',
            'delete': 'destroy'
         })
    ),
    path('schedule/', ScheduleView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('schedule/<int:pk>/',
         ScheduleView.as_view({
             'get': 'retrieve',
             'put': 'update',
             'delete': 'destroy'
         })
         ),
    path('financial-metrics/', FinancialMetricsView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('financial-metrics/<int:pk>/', FinancialMetricsView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('analytics/', AnalyticsView.as_view({
        'get' : 'get_analytics'
    })),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', index, name='index'),
]