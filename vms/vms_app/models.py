from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.db.models import Sum

# Create your models here.

class Vendor(models.Model):
    vendor_code = models.CharField(
        primary_key=True, max_length=20, editable=False)
    name = models.CharField(max_length=100)
    contact_details = models.TextField(max_length=255)
    address = models.TextField(max_length=255)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    # def __str__(self):
    #     return f"Vendor {self.name}: {self.vendor_code}"

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = get_random_string(length=20)
            while Vendor.objects.filter(vendor_code=self.vendor_code).exists():
                self.vendor_code = get_random_string(length=20)

    def calculate_and_update_metrics(self):
        print("Calculate method called")
        completed_orders = PurchaseOrder.objects.filter(
            vendor=self, status='completed').exclude(quality_rating=None)

        # Calculate on-time delivery rate
        on_time_delivered = completed_orders.filter(
            delivery_date__lte=models.F('acknowledgement_date')).count()
        total_completed_orders = completed_orders.count()
        self.on_time_delivery_rate = (
            on_time_delivered / total_completed_orders) * 100 if total_completed_orders > 0 else 0

        # Calculate quality rating average
        total_quality_ratings = completed_orders.aggregate(Sum('quality_rating'))['quality_rating__sum']

        self.quality_rating_avg = total_quality_ratings / \
            total_completed_orders if total_completed_orders > 0 else 0

        # Calculate average response time
        response_times = []
        for order in completed_orders:
            if order.acknowledgement_date:
                response_time = order.acknowledgement_date - order.issue_date
                # Convert seconds to hours
                response_times.append(response_time.total_seconds() / 3600)

        average_response_time = sum(
            response_times) / len(response_times) if response_times else 0
        self.average_response_time = average_response_time

        # Calculate fulfillment rate
        total_orders_issued = PurchaseOrder.objects.filter(vendor=self).count()
        successfully_fulfilled_orders = PurchaseOrder.objects.filter(vendor=self, status='completed').exclude(
            quality_rating=None).count()
        self.fulfillment_rate = (
            successfully_fulfilled_orders / total_orders_issued) * 100 if total_orders_issued > 0 else 0

        # Save the updated metrics
        self.save(update_fields=[
            'on_time_delivery_rate',
            'quality_rating_avg',
            'average_response_time',
            'fulfillment_rate',
        ])


class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    po_number = models.CharField(
        primary_key=True, max_length=10, editable=False)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateField()
    acknowledgement_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk and self.status == 'completed' and not PurchaseOrder.objects.filter(pk=self.pk,
                                                                                       status='completed').exists():
            super().save(*args, **kwargs)
        else:
            if not self.po_number:
                unique = False
                while not unique:
                    new_po_number = get_random_string(length=10)
                    if not PurchaseOrder.objects.filter(po_number=new_po_number).exists():
                        unique = True
                        self.po_number = new_po_number
            super().save(*args, **kwargs)


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
