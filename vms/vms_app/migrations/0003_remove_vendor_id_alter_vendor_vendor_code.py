# Generated by Django 4.1.13 on 2023-11-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms_app', '0002_alter_vendor_name_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='id',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
