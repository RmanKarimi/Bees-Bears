from rest_framework.exceptions import ValidationError

from customer.serializers import CustomerSerializer
from customer.tests.base import CustomerTestBase


class CustomerSerializerTest(CustomerTestBase):
    def setUp(self):
        super().setUp()
        self.valid_data = {
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice.smith@example.com",
            "phone": "+1234567890",
            "address": "123 Main St",
        }
        self.serializer = CustomerSerializer(data=self.valid_data)

    def test_valid_data_serialization(self):
        self.assertTrue(self.serializer.is_valid())
        validated = self.serializer.validated_data
        self.assertEqual(validated["first_name"], "Alice")
        self.assertEqual(validated["last_name"], "Smith")
        self.assertEqual(validated["email"], "alice.smith@example.com")
        self.assertEqual(validated["phone"], "+1234567890")
        self.assertEqual(validated["address"], "123 Main St")

    def test_invalid_phone(self):
        self.valid_data["phone"] = "invalid-phone"
        serializer = CustomerSerializer(data=self.valid_data)
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        self.assertIn("Phone number must contain 10–15 digits", str(cm.exception))

    def test_short_address(self):
        self.valid_data["address"] = "Short"
        serializer = CustomerSerializer(data=self.valid_data)
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        self.assertIn("Address seems too short", str(cm.exception))
