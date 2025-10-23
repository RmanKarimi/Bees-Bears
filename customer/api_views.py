from rest_framework import mixins
from customer.models import Customer
from customer.serializers import CustomerSerializer
from common.views import BaseViewSet


class CustomerViewSet(
    BaseViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
