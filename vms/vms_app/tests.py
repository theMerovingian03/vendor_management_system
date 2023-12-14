from rest_framework.test import APITestCase
from rest_framework import status
from .models import Vendor  

# class VendorProfileTests(APITestCase):
#     def setUp(self):
#         self.data = {
#             'name': 'VendorXYZ',
#             'contact_details': 'vendor_xyz@example.com',
#             'address': '123 Vendor Street',
#             'on_time_delivery_rate': 95.5,
#             'quality_rating_avg': 4.2,
#             'average_response_time': 12.5,
#             'fulfillment_rate': 98.7
#         }

#         self.vendor = Vendor.objects.create(**self.data)

#     def test_create_vendor(self):
#         response = self.client.post('/api/vendors/', self.data, format='json')
#         print("created vendor such as: ")
#         print(response.content)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_list_vendors(self):
#         response = self.client.get('/api/vendors/')
#         print(response.content)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_retrieve_vendor_details(self):
#         # response = self.client.get(f'/api/vendors/{self.vendor.vendor_code}/')
#         response = self.client.get(f'/api/vendors/{self.vendor.vendor_code}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

class VendorProfileTests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.data = {
            'name':'VendorXYZ',
            'contact_details':'vendor_xyz@example.com',
            'address':'123 Vendor Street',
            'on_time_delivery_rate': 95.5,
            'quality_rating_avg': 4.2,
            'average_response_time': 12.5,
            'fulfillment_rate': 98.7
        }

        cls.vendor = Vendor.objects.create(**cls.data)

    def test_create_vendor_api(self):
        api_data = {
            'name':'VendorABC',
            'contact_details': 'vendorabc@example.com',
            'address': '498 Elm Street',
            'on_time_delivery_rate': 90.0,
            'quality_rating_avg': 4.5,
            'average_response_time': 15.0,
            'fulfillment_rate': 96.0
        }
        response = self.client.post('/api/vendors/', api_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_vendor_details(self):
        response = self.client.get(f'/api/vendors/{self.vendor.vendor_code}')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_vendors(self):
        response = self.client.get('/api/vendors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)