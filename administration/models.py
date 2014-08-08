# coding=utf-8
from django.db import models


USAGE_CHOICE = (
    ('1', '使用'),
    ('0', '闲置')
)


class Asset(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField(max_length=100, blank=True, null=True)
    regtime = models.DateField(null=True, blank=True)
    categories = models.ManyToManyField('administration.AssetCategory')
    group = models.ForeignKey('hr.Department', blank=True, null=True, on_delete=models.SET_NULL)
    usage = models.CharField(max_length=1, choices=USAGE_CHOICE)

    def __unicode__(self):
        return "%s-%s" % (self.brand, self.model)


class AssetCategory(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=100, blank=True)
    label = models.ForeignKey('system.Label', blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name

