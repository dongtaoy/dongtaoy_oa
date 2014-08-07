__author__ = 'dongtaoy'
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission



class Sidebar(models.Model):
    name = models.CharField(max_length=45, blank=True)
    url = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)

    def __unicode__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length='50', null=True, blank=True)
    css = models.CharField(max_length='50', null=True, blank=True)

    def __unicode__(self):
        return self.name


class PermissionProfile(models.Model):
    app = models.CharField(max_length=45, blank=True)
    model = models.CharField(max_length=45, blank=True)
    action = models.CharField(max_length=45, blank=True)
    permission = models.OneToOneField('auth.Permission', null=True, blank=True)
    content = models.ForeignKey(ContentType, blank=True, null=True, on_delete=models.SET_NULL)
    Sidebar = models.ForeignKey(Sidebar, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return "%s %s %s" % (self.app, self.action, self.model)
