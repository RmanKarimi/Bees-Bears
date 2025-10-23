from django.test import TestCase

from rest_framework.exceptions import ValidationError

from account.serializers import RegisterSerializer
from django.contrib.auth.models import User


class RegisterSerializerTest(TestCase):
    def setUp(self):
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
        serializer = RegisterSerializer(data=self.valid_payload)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, self.valid_payload["username"])
        self.assertEqual(user.email, self.valid_payload["email"])

    def test_invalid_username(self):
        self.invalid_payload["username"] = "invalid username!"
        serializer = RegisterSerializer(data=self.invalid_payload)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn("username", serializer.errors)

    def test_invalid_email(self):
        self.invalid_payload["email"] = "invalid-email"
        serializer = RegisterSerializer(data=self.invalid_payload)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn("email", serializer.errors)

    def test_invalid_password(self):
        serializer = RegisterSerializer(data=self.invalid_payload)
        self.assertFalse(serializer.is_valid())
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
