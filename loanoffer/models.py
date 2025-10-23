import uuid
from django.db import models
from common.models import BaseModel
from customer.models import Customer
from loanoffer.utils import calculate_monthly_payment


class LoanOffer(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="loans"
    )
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    term_months = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()

    def __str__(self):
        return f"Loan {self.id} for {self.customer.first_name} {self.customer.last_name}    "

    @property
    def monthly_payment(self):
        return calculate_monthly_payment(
            self.amount, self.interest_rate, self.term_months
        )


# TODO: implement logic to generate amortization schedule
