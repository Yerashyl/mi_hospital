import datetime
from api.models import Appointment

def get_upcoming_appointments_count():
    return Appointment.objects.filter(
        date_time__gte=datetime.datetime.now() - datetime.timedelta(days=1)
    ).count()