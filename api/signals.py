import datetime

from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from api.models import Appointment, Notification, Doctor, Patient

@receiver(post_save, sender=Appointment)
def notification_new_appointment(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            sender=instance.patient.user,
            recipient=instance.schedule.doctor.user,
            message="New appointment created",
            notification_type=Notification.APPOINTMENT_CREATED,
        )


@receiver(pre_save, sender=Appointment)
def notification_old_appointment(sender, instance, **kwargs):
    if instance.status == Appointment.CANCELLED:
        Notification.objects.create(
            sender=instance.patient.user,
            recipient=instance.schedule.doctor.user,
            message="Appointment cancelled",
            notification_type=Notification.APPOINTMENT_CANCELLED,
        )


@receiver(pre_delete, sender=Doctor)
def notification_delete_doctor(sender, instance, **kwargs):
    upcoming_appointment_users_id = Appointment.objects.filter(
        date_time__gt=datetime.date.today(),
        doctor=instance
    ).values_list('patient__user_id', flat=True)
    for user_id in upcoming_appointment_users_id:
        Notification.objects.create(
            sender=instance.user,
            recipient_id=user_id,
            message=f"Doctor {instance.full_name} was deleted, all schedules and appointments were cancelled",
            notification_type=Notification.OTHER
        )


@receiver(pre_delete, sender=Patient)
def notification_delete_patient(sender, instance, **kwargs):
    related_appointments = Appointment.objects.filter(patient=instance)
    for appointment in related_appointments:
        Notification.objects.create(
            sender=instance.user,
            recipient=appointment.schedule.doctor.user,
            message=f"Patient {instance.full_name} was deleted, all appointments were cancelled",
            notification_type=Notification.OTHER
        )