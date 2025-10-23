from django.urls import path, include

from rest_framework import routers

from loanoffer.api_views import LoanOfferViewSet

router = routers.DefaultRouter()
router.register(r"loanoffers", LoanOfferViewSet, basename="loanoffers")

urlpatterns = [
    path("", include(router.urls)),
]
