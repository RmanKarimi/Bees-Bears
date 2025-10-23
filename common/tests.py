# loanoffer/tests/base.py
from decimal import Decimal
from datetime import date
from django.test import TestCase
from django.contrib.auth import get_user_model
from customer.models import Customer
from loanoffer.models import LoanOffer

User = get_user_model()


class TestBase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user1", password="pass")
        self.superuser = User.objects.create_superuser(
            username="admin", password="pass"
        )
        self.customer = Customer.objects.create(
            created_by=self.user,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="+1234567890",
            address="123 Main St",
        )
        self.loan = LoanOffer.objects.create(
            customer=self.customer,
            amount=Decimal("1000"),
            interest_rate=Decimal("5"),
            term_months=12,
            description="Test loan",
            start_date=date.today(),
            created_by=self.user,
        )
