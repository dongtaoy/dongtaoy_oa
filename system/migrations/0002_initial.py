# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sidebar'
        db.create_table(u'system_sidebar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(max_length=1, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Sidebar'], null=True, blank=True)),
        ))
        db.send_create_signal(u'system', ['Sidebar'])

        # Adding model 'Label'
        db.create_table(u'system_label', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='50', null=True, blank=True)),
            ('css', self.gf('django.db.models.fields.CharField')(max_length='50', null=True, blank=True)),
        ))
        db.send_create_signal(u'system', ['Label'])

        # Adding model 'PermissionProfile'
        db.create_table(u'system_permissionprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('permission_name', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('permission', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.Permission'], unique=True, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('Sidebar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Sidebar'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'system', ['PermissionProfile'])


    def backwards(self, orm):
        # Deleting model 'Sidebar'
        db.delete_table(u'system_sidebar')

        # Deleting model 'Label'
        db.delete_table(u'system_label')

        # Deleting model 'PermissionProfile'
        db.delete_table(u'system_permissionprofile')


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
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.Permission']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'permission_name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'})
        },
        u'system.sidebar': {
            'Meta': {'object_name': 'Sidebar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Sidebar']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['system']