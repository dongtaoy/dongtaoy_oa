from __future__ import unicode_literals

from django.db import models

class OaGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'oa_group'

class OaGroupPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    permission = models.ForeignKey('OaPermission', db_column='permission', blank=True, null=True)
    group = models.ForeignKey(OaGroup, db_column='group', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'oa_group_permission'

class OaPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    parentid = models.ForeignKey('self', db_column='parentid', blank=True, null=True)
    name = models.CharField(max_length=45)
    url = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'oa_permission'

class OaUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=45, blank=True)
    password = models.CharField(max_length=45, blank=True)
    realname = models.CharField(max_length=45, blank=True)
    sex = models.IntegerField(blank=True, null=True)
    regtime = models.IntegerField(blank=True, null=True)
    regip = models.CharField(max_length=15, blank=True)
    lastime = models.IntegerField(blank=True, null=True)
    lastip = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'oa_user'

class OaUserGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.ForeignKey(OaUser, db_column='userid')
    groupid = models.ForeignKey(OaGroup, db_column='groupid')
    class Meta:
        managed = False
        db_table = 'oa_user_group'