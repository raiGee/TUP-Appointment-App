# Generated by Django 3.2.8 on 2022-01-28 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineAppointmentApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='email',
            new_name='emails',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='password',
            new_name='passwords',
        ),
    ]