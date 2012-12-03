# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Order'
        db.delete_table('chimareports_order')

        # Adding model 'DisplayField'
        db.create_table('chimareports_displayfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('queryset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chimareports.Queryset'])),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('field_verbose', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('sort', self.gf('django.db.models.fields.CharField')(default=None, max_length=4, null=True, blank=True)),
            ('annotate', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('chimareports', ['DisplayField'])

        # Adding field 'QueryFilter.field_verbose'
        db.add_column('chimareports_queryfilter', 'field_verbose',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Order'
        db.create_table('chimareports_order', (
            ('field', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('queryset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chimareports.Queryset'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('chimareports', ['Order'])

        # Deleting model 'DisplayField'
        db.delete_table('chimareports_displayfield')

        # Deleting field 'QueryFilter.field_verbose'
        db.delete_column('chimareports_queryfilter', 'field_verbose')


    models = {
        'chimareports.displayfield': {
            'Meta': {'object_name': 'DisplayField'},
            'annotate': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'field_verbose': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'queryset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chimareports.Queryset']"}),
            'sort': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'chimareports.queryfilter': {
            'Meta': {'object_name': 'QueryFilter'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'field_verbose': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lookup': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'queryset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chimareports.Queryset']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'value_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'chimareports.queryset': {
            'Meta': {'object_name': 'Queryset'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['chimareports']