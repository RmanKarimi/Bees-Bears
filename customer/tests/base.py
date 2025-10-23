from django.test import TestCase
from django.contrib.auth import get_user_model
from customer.models import Customer

User = get_user_model()


class CustomerTestBase(TestCase):
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
