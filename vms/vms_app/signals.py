from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_on_time_delivery_rate(sender, instance, created, **kwargs):
    if created or instance.status == 'completed':
        if created:
            print("New order created")
        elif instance.status == 'completed':
            print("PO status marked as completed")
        vendor = instance.vendor
        vendor.calculate_and_update_metrics()
        # print('Completion ack')
