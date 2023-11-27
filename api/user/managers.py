from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from .enums import ROLE_CHOICE
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):
    # """
    # Custom user model manager where username is the unique identifiers
    # """

    # def create_user_with_phone_number(self, phone_number, username, **extra_fields):
    #     """
    #     Create and save a User with the given username and password.
    #     """
    #     if not phone_number:
    #         raise ValueError(_('You did not set phone_number'))
    #     user = self.model(phone_number=phone_number, username=username, is_active=True,
    #                       roles = [SystemRoleEnum.COACH,], **extra_fields)
    #     user.save()
    #     return user

    def create_user(self, username, password, **extra_fields):
        """
        Create and save a User with the given phone_number and password.
        """
        
        user = self.model( username=username, **extra_fields)
        user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone_number and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        user = self.create_user(username, password, **extra_fields)
        user.roles = ['admin',]
        user.save()