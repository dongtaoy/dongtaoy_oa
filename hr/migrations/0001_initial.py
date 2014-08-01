# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'hr_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('realname', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('sex', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('regtime', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('lastlogin', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('lastip', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('salary', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('endtime', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('salt', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hr.Userstatus'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'hr', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'hr_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'hr.user'], null=False)),
            ('group', models.ForeignKey(orm[u'hr.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding model 'Group'
        db.create_table(u'hr_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('leader', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['hr.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'hr', ['Group'])

        # Adding M2M table for field permissions on 'Group'
        m2m_table_name = db.shorten_name(u'hr_group_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm[u'hr.group'], null=False)),
            ('permission', models.ForeignKey(orm[u'system.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['group_id', 'permission_id'])

        # Adding model 'Userstatus'
        db.create_table(u'hr_userstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal(u'hr', ['Userstatus'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'hr_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'hr_user_groups'))

        # Deleting model 'Group'
        db.delete_table(u'hr_group')

        # Removing M2M table for field permissions on 'Group'
        db.delete_table(db.shorten_name(u'hr_group_permissions'))

        # Deleting model 'Userstatus'
        db.delete_table(u'hr_userstatus')


    models = {
        u'hr.group': {
            'Meta': {'object_name': 'Group'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'label': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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

    complete_apps = ['hr']