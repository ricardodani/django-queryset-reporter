# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Queryset'
        db.create_table('chimareports_queryset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('chimareports', ['Queryset'])

        # Adding model 'QueryFilter'
        db.create_table('chimareports_queryfilter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('queryset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chimareports.Queryset'])),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('lookup', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('value_2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal('chimareports', ['QueryFilter'])

        # Adding model 'Order'
        db.create_table('chimareports_order', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('queryset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chimareports.Queryset'])),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('chimareports', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Queryset'
        db.delete_table('chimareports_queryset')

        # Deleting model 'QueryFilter'
        db.delete_table('chimareports_queryfilter')

        # Deleting model 'Order'
        db.delete_table('chimareports_order')


    models = {
        'chimareports.order': {
            'Meta': {'object_name': 'Order'},
            'desc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'queryset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chimareports.Queryset']"})
        },
        'chimareports.queryfilter': {
            'Meta': {'object_name': 'QueryFilter'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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