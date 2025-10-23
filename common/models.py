from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
