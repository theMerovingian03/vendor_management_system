from django.urls import path
from . import views

urlpatterns = [
    path('vendors/<str:vendor_code>/', views.VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/', views.VendorListCreateView.as_view(), name='vendor-list-create'),
    path('purchase_orders/', views.PurchaseOrderListCreateView.as_view(), name='purchase-orders-list-create'),
    path('purchase_orders/<str:po_number>', views.PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('vendors/<str:vendor_code>/performance/', views.VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/<str:po_number>/acknowledge/', views.AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase'),
]