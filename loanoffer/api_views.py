from rest_framework import mixins
from loanoffer.models import LoanOffer
from loanoffer.serializers import LoanOfferSerializer
from common.views import BaseViewSet


class LoanOfferViewSet(
    BaseViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):
    queryset = LoanOffer.objects.all()
    serializer_class = LoanOfferSerializer
