# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Queryset'
        db.create_table('queryset_reporter_queryset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('desc', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
            ('model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('queryset_reporter', ['Queryset'])

        # Adding model 'DisplayField'
        db.create_table('queryset_reporter_displayfield', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('queryset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['queryset_reporter.Queryset'])),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('field_verbose', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('sort', self.gf('django.db.models.fields.CharField')(default=None, max_length=4, null=True, blank=True)),
            ('annotate', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('queryset_reporter', ['DisplayField'])

        # Adding model 'QueryFilter'
        db.create_table('queryset_reporter_queryfilter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('queryset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['queryset_reporter.Queryset'])),
            ('field', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('field_verbose', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('lookup', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('value_2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=7)),
        ))
        db.send_create_signal('queryset_reporter', ['QueryFilter'])


    def backwards(self, orm):
        # Deleting model 'Queryset'
        db.delete_table('queryset_reporter_queryset')

        # Deleting model 'DisplayField'
        db.delete_table('queryset_reporter_displayfield')

        # Deleting model 'QueryFilter'
        db.delete_table('queryset_reporter_queryfilter')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'queryset_reporter.displayfield': {
            'Meta': {'ordering': "['position']", 'object_name': 'DisplayField'},
            'annotate': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'field_verbose': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'queryset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['queryset_reporter.Queryset']"}),
            'sort': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'queryset_reporter.queryfilter': {
            'Meta': {'object_name': 'QueryFilter'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'field_verbose': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lookup': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'queryset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['queryset_reporter.Queryset']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'value_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'queryset_reporter.queryset': {
            'Meta': {'object_name': 'Queryset'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['queryset_reporter']