from decimal import Decimal
from datetime import date

from loanoffer.models import LoanOffer, calculate_monthly_payment
from loanoffer.tests.base import LoanOfferTestBase


class LoanOfferModelTest(LoanOfferTestBase):
    def test_monthly_payment_calculation_with_interest(self):
        loan = LoanOffer.objects.create(
            customer=self.customer,
            amount=Decimal("12000.00"),
            interest_rate=Decimal("12.0"),
            term_months=12,
            description="Test loan",
            start_date=date.today(),
        )
        expected = calculate_monthly_payment(Decimal("12000.00"), Decimal("12.0"), 12)
        self.assertEqual(loan.monthly_payment, expected)

    def test_monthly_payment_calculation_zero_interest(self):
        loan = LoanOffer.objects.create(
            customer=self.customer,
            amount=Decimal("12000.00"),
            interest_rate=Decimal("0.0"),
            term_months=12,
            description="Zero interest loan",
            start_date=date.today(),
        )
        expected = Decimal("12000.00") / 12
        self.assertEqual(loan.monthly_payment, expected)

    def test_monthly_payment_invalid_term_raises(self):
        with self.assertRaises(ValueError):
            calculate_monthly_payment(Decimal("1000"), Decimal("5.0"), 0)
