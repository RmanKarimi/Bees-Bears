from django.test import TestCase

from rest_framework.test import APIClient

from rest_framework import status


class RegisterViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "Test1234!",
            "password_confirm": "Test1234!",
        }
        self.invalid_payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "Test1234!",
            "password_confirm": "DifferentPassword123!",
        }

    def test_valid_registration(self):
        response = self.client.post("/auth/register/", self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("username", response.data)

    def test_invalid_registration(self):
        response = self.client.post("/auth/register/", self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
