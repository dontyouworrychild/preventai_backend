import os
import uuid
from datetime import datetime, timezone


from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.base_user import BaseUserManager
from .managers import CustomUserManager

from .managers import CustomUserManager
from .enums import ROLE_CHOICE

def default_role():
    return ["admin"]

def image_directory_path(instance, filename):
    role = "other"
    if hasattr(instance, 'role'):
        role = instance.role

    extension = filename.split('.')[-1]
    return f"{role}/{instance.id}.{extension}"

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        _("username"),
        max_length=50,
        unique=True,
        validators=[RegexValidator(
                regex='^[a-z0-9_]+$',
                message='Username can only contain lowercase letters, numbers, and underscores.',
                code='invalid_username'
            ),
        ],
    )
    image = models.ImageField(upload_to=image_directory_path, blank=True, null=True)
    first_name = models.CharField(_("first_name"), max_length=150, blank=True)
    last_name = models.CharField(_("last_name"), max_length=150, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["phone_number"]
    objects = CustomUserManager()
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, null=True, blank=True)
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.username}: {self.role}"