# Generated by Django 3.2.8 on 2022-02-01 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineAppointmentApp', '0003_registration_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('fullnames', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('timess', models.CharField(max_length=100)),
                ('DEPT', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
            ],
        ),
    ]
