# Generated by Django 4.1.13 on 2023-11-28 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms_app', '0005_vendor_on_time_delivery_rate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistorialPerformance',
            new_name='HistoricalPerformance',
        ),
    ]
