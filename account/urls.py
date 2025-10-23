from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from account.api_views import RegisterViewSet

urlpatterns = [
    path("register/", RegisterViewSet.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
