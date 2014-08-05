# coding=utf-8
from django.db import models
from django.contrib import admin

SEX_CHOICE = (
    ('1', '男'),
    ('0', '女'),
)


class Employee(models.Model):
    realname = models.CharField(max_length=45, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICE)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=45, blank=True)
    salary = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=45, blank=True)
    dob = models.DateField(blank=True, null=True)
    identifier = models.CharField(max_length=45, blank=True)
    address = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey('hr.UserStatus', blank=True, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField('auth.User')

    def __unicode__(self):
        return self.realname


class Department(models.Model):
    description = models.TextField()
    leader = models.ForeignKey('hr.Employee', blank=True, null=True)
    label = models.ForeignKey('system.Label', blank=True, null=True, default=None, on_delete=models.SET_NULL)
    group = models.OneToOneField('auth.Group')

    def __unicode__(self):
        return self.group.name


class UserStatus(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    label = models.ForeignKey('system.Label', blank=True, null=True, default=None, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(UserStatus)