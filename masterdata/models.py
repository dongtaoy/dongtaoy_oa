from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    regtime = models.DateField(blank=True, null=True)
    type = models.ForeignKey('masterdata.MatirialType', blank=True, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey('hr.User', blank=True, null=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField('hr.Group', blank=True, null=True)


class MaterialType(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True, null=True)
    label = models.ForeignKey('system.Label', blank=True, null=True, on_delete=models.SET_NULL)