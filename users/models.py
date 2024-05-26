from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name=_('EMAIL'))
    phone = PhoneNumberField(verbose_name=_('Phone number'), **NULLABLE)
    city = models.CharField(max_length=200, verbose_name=_('City'), **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
