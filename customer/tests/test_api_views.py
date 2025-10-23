from rest_framework.test import APIClient
from rest_framework import status

from customer.models import Customer
from customer.tests.base import CustomerTestBase


class CustomerViewSetTest(CustomerTestBase):
    def setUp(self):
        super().setUp()
        self.client = APIClient()

    def test_list_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/customers/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_list_superuser_sees_all(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get("/customers/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_customer(self):
        self.client.force_authenticate(user=self.user)
        payload = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "phone": "+19876543210",
            "address": "456 Elm St",
        }
        response = self.client.post("/customers/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.filter(created_by=self.user).count(), 2)

    def test_retrieve_customer(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f"/customers/{self.customer.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["first_name"], "John")
        self.assertEqual(response.data["last_name"], "Doe")

    def test_unauthenticated_access_denied(self):
        response = self.client.get("/customers/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
