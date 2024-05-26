from django.db import models
from django.utils.translation import gettext_lazy as _


class Organization(models.Model):
    title = models.CharField(verbose_name=_('Organization'))
    email = models.EmailField(verbose_name=_('EMAIL'))
    country = models.CharField(verbose_name=_('Country'))
    city = models.CharField(verbose_name=_('City'))
    street = models.CharField(verbose_name=_('Street'))
    building_number = models.CharField(verbose_name=_('Building number'))
    supplier = models.ManyToManyField(to='Organization', verbose_name=_('Supplier'))
    debt = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_('Debt to supplier'), default=0.00)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of creation'))


class Product(models.Model):
    manufacturer = models.ForeignKey(to=Organization, on_delete=models.SET_NULL,
                                     verbose_name=_('Manufacturer'), related_name='manufacturer', null=True)
    seller = models.ForeignKey(to=Organization, on_delete=models.SET_NULL,
                               verbose_name=_('Seller'), related_name='seller', null=True)
    title = models.CharField(max_length=300, verbose_name=_('Product title'))
    model = models.CharField(max_length=100, verbose_name=_('Model'))
    release_date = models.DateField(verbose_name=_('Release date'))
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_('Price'))
