from django.contrib import admin

from loanoffer.models import LoanOffer


@admin.register(LoanOffer)
class LoanOfferAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "amount",
        "interest_rate",
        "term_months",
        "start_date",
        "monthly_payment",
    )
    search_fields = ("customer__first_name", "customer__last_name", "customer__email")
    list_filter = ("interest_rate", "term_months", "start_date")
