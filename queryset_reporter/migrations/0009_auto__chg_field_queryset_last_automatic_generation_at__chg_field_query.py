# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Queryset.last_automatic_generation_at'
        db.alter_column('queryset_reporter_queryset', 'last_automatic_generation_at', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Queryset.last_automatic_generation_xlsx'
        db.alter_column('queryset_reporter_queryset', 'last_automatic_generation_xlsx', self.gf('django.db.models.fields.CharField')(max_length=250, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Queryset.last_automatic_generation_at'
        raise RuntimeError("Cannot reverse this migration. 'Queryset.last_automatic_generation_at' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Queryset.last_automatic_generation_xlsx'
        raise RuntimeError("Cannot reverse this migration. 'Queryset.last_automatic_generation_xlsx' and its values cannot be restored.")

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
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'field_verbose': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'queryset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['queryset_reporter.Queryset']"}),
            'sort': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        'queryset_reporter.queryfilter': {
            'Meta': {'object_name': 'QueryFilter'},
            'field': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'field_verbose': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lookup': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'queryset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['queryset_reporter.Queryset']"}),
            'readonly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'value_0': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'value_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'queryset_reporter.queryset': {
            'Meta': {'object_name': 'Queryset'},
            'automatic_generation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'distinct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_automatic_generation_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_automatic_generation_xlsx': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'model': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['queryset_reporter']