# coding=utf-8
from django.db import models

SEX_CHOICE = (
    ('1', '男'),
    ('0', '女'),
)


class Employee(models.Model):
    sex = models.CharField(max_length=1, choices=SEX_CHOICE)
    phone = models.CharField(max_length=45, blank=True)
    salary = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=45, blank=True)
    dob = models.DateField(blank=True, null=True)
    identifier = models.CharField(max_length=45, blank=True)
    address = models.CharField(max_length=100, blank=True)
    status = models.ForeignKey('hr.UserStatus', blank=True, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField('auth.User')
    description = models.TextField(blank=True)

    class Meta:
        permissions = (('change_own_password', 'Can change own password'),)

    def __unicode__(self):
        return self.user.last_name + self.user.first_name

    def full_name(self):
        return self.user.last_name + self.user.first_name


class Department(models.Model):
    leader = models.ForeignKey('hr.Employee', blank=True, null=True)
    label = models.ForeignKey('system.Label', blank=True, null=True, default=None, on_delete=models.SET_NULL)
    group = models.OneToOneField('auth.Group')
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.group.name


class UserStatus(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    label = models.ForeignKey('system.Label', blank=True, null=True, default=None, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name
