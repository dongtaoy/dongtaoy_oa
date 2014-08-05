# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'public_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('fromUser', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='Message_fromUser', null=True, on_delete=models.SET_NULL, to=orm['hr.User'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.MessageType'], null=True, blank=True)),
            ('time', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'public', ['Message'])

        # Adding model 'MessageTo'
        db.create_table(u'public_messageto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Message'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hr.User'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('read', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('delete', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'public', ['MessageTo'])

        # Adding model 'MessageType'
        db.create_table(u'public_messagetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'public', ['MessageType'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'public_message')

        # Deleting model 'MessageTo'
        db.delete_table(u'public_messageto')

        # Deleting model 'MessageType'
        db.delete_table(u'public_messagetype')


    models = {
        u'hr.group': {
            'Meta': {'object_name': 'Group'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['system.Label']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'leader': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['hr.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['system.Permission']", 'null': 'True', 'blank': 'True'})
        },
        u'hr.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'endtime': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hr.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'lastip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'lastlogin': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'realname': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'regtime': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'sex': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hr.Userstatus']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'hr.userstatus': {
            'Meta': {'object_name': 'Userstatus'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['system.Label']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'public.message': {
            'Meta': {'object_name': 'Message'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'fromUser': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'Message_fromUser'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['hr.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'toUser': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Message_toUser'", 'to': u"orm['hr.User']", 'through': u"orm['public.MessageTo']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.MessageType']", 'null': 'True', 'blank': 'True'})
        },
        u'public.messageto': {
            'Meta': {'object_name': 'MessageTo'},
            'delete': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Message']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'read': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hr.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        u'public.messagetype': {
            'Meta': {'object_name': 'MessageType'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'system.label': {
            'Meta': {'object_name': 'Label'},
            'css': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'})
        },
        u'system.permission': {
            'Meta': {'object_name': 'Permission'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Permission']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['public']