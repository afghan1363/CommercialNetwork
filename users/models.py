from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from comm_net_app.models import Organization

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name=_('EMAIL'))
    phone = PhoneNumberField(verbose_name=_('Phone number'), **NULLABLE)
    city = models.CharField(max_length=200, verbose_name=_('City'), **NULLABLE)
    organization = models.ForeignKey(to=Organization, on_delete=models.CASCADE, verbose_name=_('Organization'),
                                     related_name='employee', **NULLABLE)
    moderator = models.BooleanField(verbose_name=_('Moderator'), default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
