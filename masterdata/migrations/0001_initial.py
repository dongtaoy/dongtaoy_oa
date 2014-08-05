# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Material'
        db.create_table(u'masterdata_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('regtime', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['masterdata.MaterialType'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hr.User'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'masterdata', ['Material'])

        # Adding M2M table for field groups on 'Material'
        m2m_table_name = db.shorten_name(u'masterdata_material_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('material', models.ForeignKey(orm[u'masterdata.material'], null=False)),
            ('group', models.ForeignKey(orm[u'hr.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['material_id', 'group_id'])

        # Adding model 'MaterialType'
        db.create_table(u'masterdata_materialtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('label', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['system.Label'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'masterdata', ['MaterialType'])


    def backwards(self, orm):
        # Deleting model 'Material'
        db.delete_table(u'masterdata_material')

        # Removing M2M table for field groups on 'Material'
        db.delete_table(db.shorten_name(u'masterdata_material_groups'))

        # Deleting model 'MaterialType'
        db.delete_table(u'masterdata_materialtype')


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
        u'masterdata.material': {
            'Meta': {'object_name': 'Material'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hr.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'regtime': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['masterdata.MaterialType']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hr.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'})
        },
        u'masterdata.materialtype': {
            'Meta': {'object_name': 'MaterialType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['system.Label']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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

    complete_apps = ['masterdata']