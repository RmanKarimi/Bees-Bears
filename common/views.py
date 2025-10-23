from rest_framework import viewsets, permissions
from common.mixins import UserOwnedQuerysetMixin


class BaseViewSet(UserOwnedQuerysetMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
