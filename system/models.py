__author__ = 'dongtaoy'
from django.db import models


class Permission(models.Model):
    name = models.CharField(max_length=45, blank=True)
    url = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)


class Label(models.Model):
    name = models.CharField(max_length='50', null=True, blank=True)
    css = models.CharField(max_length='50', null=True, blank=True)
