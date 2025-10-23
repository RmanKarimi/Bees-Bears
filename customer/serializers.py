import re

from rest_framework import serializers

from common.serializers import UserOwnedSerializer
from customer.models import Customer


class CustomerSerializer(UserOwnedSerializer):
    phone = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    address = serializers.CharField(allow_blank=True, allow_null=True, required=False)

    def validate_phone(self, value):
        if value:
            if not re.match(r"^\+?\d{10,15}$", value):
                raise serializers.ValidationError(
                    "Phone number must contain 10–15 digits and may start with +."
                )
        return value

    def validate_address(self, value):
        if value and len(value.strip()) < 10:
            raise serializers.ValidationError("Address seems too short.")
        return value

    class Meta:
        model = Customer
        fields = ["id", "first_name", "last_name", "email", "phone", "address"]
