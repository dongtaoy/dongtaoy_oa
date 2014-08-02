__author__ = 'kay'
from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=45)
    phone = models.IntegerField(max_length=15, blank=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    email = models.CharField(max_length=50,blank=True)
    fax = models.IntegerField(blank=True,null=True)
    ctype = models.ForeignKey('crm.Ctype', blank=True, null=True, default=None)


class Ctype(models.Model):
    name = models.CharField(max_length=20)
    description = address = models.CharField(max_length=100,blank=True, null=True)
    label = models.CharField(max_length=20,blank=True, null=True)