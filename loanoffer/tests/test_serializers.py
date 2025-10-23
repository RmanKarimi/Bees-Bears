from decimal import Decimal
from datetime import date
from rest_framework.exceptions import ValidationError

from loanoffer.models import LoanOffer
from loanoffer.serializers import LoanOfferSerializer
from loanoffer.tests.base import LoanOfferTestBase


class LoanOfferSerializerTest(LoanOfferTestBase):
    def setUp(self):
        super().setUp()
        self.valid_data = {
            "customer": self.customer.id,
            "amount": Decimal("10000.00"),
            "interest_rate": Decimal("5.5"),
            "term_months": 12,
            "description": "Solar panel financing",
            "start_date": date.today(),
        }

    def test_valid_data_serialization(self):
        serializer = LoanOfferSerializer(data=self.valid_data)
        self.assertTrue(serializer.is_valid())
        validated = serializer.validated_data
        self.assertEqual(validated["amount"], Decimal("10000.00"))
        self.assertEqual(validated["interest_rate"], Decimal("5.5"))
        self.assertEqual(validated["term_months"], 12)

    def test_invalid_amount(self):
        self.valid_data["amount"] = Decimal("0")
        serializer = LoanOfferSerializer(data=self.valid_data)
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        self.assertIn("Loan amount must be positive", str(cm.exception))

    def test_negative_interest_rate(self):
        self.valid_data["interest_rate"] = Decimal("-1.0")
        serializer = LoanOfferSerializer(data=self.valid_data)
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        self.assertIn("Interest rate cannot be negative", str(cm.exception))

    def test_invalid_term_months(self):
        self.valid_data["term_months"] = 0
        serializer = LoanOfferSerializer(data=self.valid_data)
        with self.assertRaises(ValidationError) as cm:
            serializer.is_valid(raise_exception=True)
        self.assertIn("Loan term must be positive", str(cm.exception))

    def test_monthly_payment_read_only(self):
        self.valid_data["monthly_payment"] = Decimal("500.00")
        serializer = LoanOfferSerializer(data=self.valid_data)
        serializer.is_valid()
        self.assertNotIn("monthly_payment", serializer.validated_data)

    def test_serializes_existing_instance(self):
        offer = LoanOffer.objects.create(
            customer=self.customer,
            amount=Decimal("20000.00"),
            interest_rate=Decimal("4.0"),
            term_months=24,
            description="Battery storage loan",
            start_date=date.today(),
        )
        serializer = LoanOfferSerializer(instance=offer)
        data = serializer.data
        self.assertEqual(data["amount"], "20000.00")
        self.assertEqual(data["interest_rate"], "4.00")
        self.assertIn("monthly_payment", data)
