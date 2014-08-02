from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100, blank=True, null=True)
    regtime = models.DateField(blank=True)
    categories = models.ManyToManyField('administration.AssetCategory', blank=True, null=True)


class AssetCategory(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100, blank=True)
    label = models.CharField(max_length=100, blank=True)