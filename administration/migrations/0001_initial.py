# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Asset'
        db.create_table(u'administration_asset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('regtime', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'administration', ['Asset'])

        # Adding M2M table for field categories on 'Asset'
        m2m_table_name = db.shorten_name(u'administration_asset_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('asset', models.ForeignKey(orm[u'administration.asset'], null=False)),
            ('assetcategory', models.ForeignKey(orm[u'administration.assetcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['asset_id', 'assetcategory_id'])

        # Adding model 'AssetCategory'
        db.create_table(u'administration_assetcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'administration', ['AssetCategory'])


    def backwards(self, orm):
        # Deleting model 'Asset'
        db.delete_table(u'administration_asset')

        # Removing M2M table for field categories on 'Asset'
        db.delete_table(db.shorten_name(u'administration_asset_categories'))

        # Deleting model 'AssetCategory'
        db.delete_table(u'administration_assetcategory')


    models = {
        u'administration.asset': {
            'Meta': {'object_name': 'Asset'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['administration.AssetCategory']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'regtime': ('django.db.models.fields.DateField', [], {'blank': 'True'})
        },
        u'administration.assetcategory': {
            'Meta': {'object_name': 'AssetCategory'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        }
    }

    complete_apps = ['administration']