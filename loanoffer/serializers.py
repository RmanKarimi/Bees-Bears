from rest_framework import serializers

from common.serializers import UserOwnedSerializer

from loanoffer.models import LoanOffer


class LoanOfferSerializer(UserOwnedSerializer):
    monthly_payment = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True
    )

    class Meta:
        model = LoanOffer
        fields = [
            "id",
            "customer",
            "amount",
            "interest_rate",
            "term_months",
            "monthly_payment",
            "description",
            "start_date",
        ]

    def validate(self, data):
        if data["amount"] <= 0:
            raise serializers.ValidationError("Loan amount must be positive")
        if data["interest_rate"] < 0:
            raise serializers.ValidationError("Interest rate cannot be negative")
        if data["term_months"] <= 0:
            raise serializers.ValidationError("Loan term must be positive")
        return data
