# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PermissionProfile.app_name'
        db.delete_column(u'system_permissionprofile', 'app_name')

        # Deleting field 'PermissionProfile.permission_name'
        db.delete_column(u'system_permissionprofile', 'permission_name')

        # Adding field 'PermissionProfile.app'
        db.add_column(u'system_permissionprofile', 'app',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)

        # Adding field 'PermissionProfile.model'
        db.add_column(u'system_permissionprofile', 'model',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)

        # Adding field 'PermissionProfile.action'
        db.add_column(u'system_permissionprofile', 'action',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PermissionProfile.app_name'
        db.add_column(u'system_permissionprofile', 'app_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)

        # Adding field 'PermissionProfile.permission_name'
        db.add_column(u'system_permissionprofile', 'permission_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=45, blank=True),
                      keep_default=False)

        # Deleting field 'PermissionProfile.app'
        db.delete_column(u'system_permissionprofile', 'app')

        # Deleting field 'PermissionProfile.model'
        db.delete_column(u'system_permissionprofile', 'model')

        # Deleting field 'PermissionProfile.action'
        db.delete_column(u'system_permissionprofile', 'action')


    models = {
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'system.label': {
            'Meta': {'object_name': 'Label'},
            'css': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'})
        },
        u'system.permissionprofile': {
            'Meta': {'object_name': 'PermissionProfile'},
            'Sidebar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Sidebar']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'action': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'app': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'permission': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.Permission']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'system.sidebar': {
            'Meta': {'object_name': 'Sidebar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Sidebar']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['system']