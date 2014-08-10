from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    regtime = models.DateField(blank=True, null=True)
    type = models.ForeignKey('masterdata.MaterialType', blank=True, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey('hr.Employee', blank=True, null=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField('hr.Department', blank=True, null=True)

    def __unicode__(self):
        return self.name

class MaterialType(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True, null=True)
    label = models.ForeignKey('system.Label', blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name