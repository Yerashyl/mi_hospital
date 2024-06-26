# Generated by Django 5.0.6 on 2024-06-25 12:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_financialmetrics_appointment_completed_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('status', models.CharField(choices=[('NEW', 'New'), ('READ', 'Read'), ('ARCHIVED', 'Archived')], default='NEW', max_length=10)),
                ('notification_type', models.CharField(choices=[('APPOINTMENT_CREATED', 'Appointment Created'), ('APPOINTMENT_CANCELLED', 'Appointment Cancelled'), ('OTHER', 'Other')], default='OTHER', max_length=21)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_notifications', related_query_name='received_notification', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_notifications', related_query_name='sent_notification', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
