# Generated by Django 4.1.13 on 2023-11-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms_app', '0003_remove_vendor_id_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='id',
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(editable=False, max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(editable=False, max_length=20, primary_key=True, serialize=False),
        ),
    ]
