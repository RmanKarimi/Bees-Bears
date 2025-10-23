from rest_framework import generics
from rest_framework.permissions import AllowAny
from account.serializers import RegisterSerializer


class RegisterViewSet(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
