from django.db import models


class Asset(models.Model):
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    regtime = models.DateField(blank=True, null=True)
    categories = models.ManyToManyField('administration.AssetCategory', blank=True, null=True)
    group = models.ForeignKey('hr.Group', blank=True, null=True, on_delete=models.SET_NULL)
    usage = models.BooleanField(blank=True, default=True)


class AssetCategory(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=100, blank=True)
    label = models.CharField(max_length=100, blank=True)