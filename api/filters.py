import django_filters as filters

from .models import Doctor, Patient


class DoctorFilterSet(filters.FilterSet):
    first_name = filters.CharFilter(field_name='last_name', )
    last_name = filters.CharFilter(field_name='first_name', )
    specialty = filters.CharFilter(field_name='specialty', )
    class Meta:
        model = Doctor
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'specialty': ['exact', ],
        }

class PatientFilterSet(filters.FilterSet):
    first_name = filters.CharFilter(field_name='first_name', )
    last_name = filters.CharFilter(field_name='last_name', )
    age = filters.NumberFilter(field_name='age', )
    gender = filters.CharFilter(field_name='gender', )
    medical_history = filters.CharFilter(field_name='medical_history', )
    class Meta:
        model = Patient
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'icontains'],
            'age': ['exact', ],
            'gender': ['exact', ],
            'medical_history': ['icontains', ],
        }