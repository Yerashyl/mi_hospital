from django.db import models
from rest_framework.authtoken.admin import User


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Specialties'


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='doctors')
    schedule = models.TextField()

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    doctor = models.ForeignKey(Doctor, related_name='patients', on_delete=models.CASCADE)
    medical_history = models.TextField()

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, related_name='patient_appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name='doctor_appointments', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, related_name='service', on_delete=models.CASCADE, null=True)
    prescription = models.TextField(null=True)
    date_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])
    rating = models.IntegerField(null=True, blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    def __str__(self):
        return f"{self.doctor.full_name} - {self.patient.full_name} - {self.date_time}"

    @property
    def patient_satisfaction(self):
        return self.rating if self.rating else None

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='schedules', on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, related_name='schedules', on_delete=models.SET_NULL, null=True)
    appointment = models.ForeignKey(Appointment, related_name='schedules', on_delete=models.SET_NULL, null=True)

class FinancialMetrics(models.Model):
    income = models.DecimalField(max_digits=10, decimal_places=2)
    expenses = models.DecimalField(max_digits=10, decimal_places=2)
    profit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.profit = self.income - self.expenses
        super().save(*args, **kwargs)


class Notification(models.Model):
    NEW = 'NEW'
    READ = 'READ'
    ARCHIVED = 'ARCHIVED'

    STATUS_CHOICES = (
        (NEW, 'New'),
        (READ, 'Read'),
        (ARCHIVED, 'Archived'),
    )

    APPOINTMENT_CREATED = 'APPOINTMENT_CREATED'
    APPOINTMENT_CANCELLED = 'APPOINTMENT_CANCELLED'
    OTHER = 'OTHER'

    TYPE_CHOICES = (
        (APPOINTMENT_CREATED, 'Appointment Created'),
        (APPOINTMENT_CANCELLED, 'Appointment Cancelled'),
        (OTHER, 'Other'),
    )

    sender = models.ForeignKey(User, related_name='sent_notifications', related_query_name='sent_notification', on_delete=models.SET_NULL, null=True)
    recipient = models.ForeignKey(User, related_name='received_notifications', related_query_name='received_notification', on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW)
    notification_type = models.CharField(max_length=21, choices=TYPE_CHOICES, default=OTHER)  # Updated max_length to 21
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender} -> {self.recipient} : {self.message[:20]}"

    class Meta:
        ordering = ['-created_at']