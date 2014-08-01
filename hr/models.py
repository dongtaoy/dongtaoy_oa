from django.db import models

class User(models.Model):
    username = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    realname = models.CharField(max_length=45, blank=True)
    sex = models.IntegerField(blank=True, null=True)
    regtime = models.DateField(blank=True, null=True)
    lastlogin = models.DateField(blank=True, null=True)
    lastip = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=45, blank=True)
    salary = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=45, blank=True)
    endtime = models.DateField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    identifier = models.CharField(max_length=45, blank=True)
    address = models.CharField(max_length=100, blank=True)
    salt = models.CharField(max_length=4, blank=True)
    status = models.ForeignKey('hr.Userstatus', blank=True, null=True, on_delete=models.SET_NULL)
    groups = models.ManyToManyField('hr.Group', blank=True, null=True)


class Group(models.Model):
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    permissions = models.ManyToManyField('system.Permission', blank=True, null=True)
    leader = models.ForeignKey('hr.User', blank=True, null=True, default=None)

class Userstatus(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    label = models.CharField(max_length=45)
