import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class KaizenUser(AbstractUser):
    is_verified = models.BooleanField(default=False, blank=False, null=False)
    verification_code = models.UUIDField(default=uuid.uuid4, editable=False)
