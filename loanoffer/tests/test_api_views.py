from datetime import date
from rest_framework.test import APIClient
from rest_framework import status
from loanoffer.models import LoanOffer
from loanoffer.tests.base import LoanOfferTestBase


class LoanOfferViewSetTest(LoanOfferTestBase):
    def setUp(self):
        super().setUp()
        self.client = APIClient()

    def test_list_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/loanoffers/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_list_superuser_sees_all(self):
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get("/loanoffers/")
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_loan(self):
        self.client.force_authenticate(user=self.user)
        payload = {
            "customer": self.customer.id,
            "amount": "2000.00",
            "interest_rate": "6.0",
            "term_months": 24,
            "description": "New loan",
            "start_date": str(date.today()),
        }
        response = self.client.post("/loanoffers/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(LoanOffer.objects.filter(created_by=self.user).count(), 2)

    def test_unauthenticated_access_denied(self):
        response = self.client.get("/loanoffers/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_loan(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f"/loanoffers/{self.loan.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["amount"], "1000.00")
