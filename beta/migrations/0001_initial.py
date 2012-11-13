# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Beta'
        db.create_table('beta_beta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('is_invited', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_sent', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('invite_hash', self.gf('django.db.models.fields.CharField')(max_length=36, null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('claimed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('beta', ['Beta'])


    def backwards(self, orm):
        # Deleting model 'Beta'
        db.delete_table('beta_beta')


    models = {
        'beta.beta': {
            'Meta': {'ordering': "('-date_sent',)", 'object_name': 'Beta'},
            'claimed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_sent': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_hash': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'is_invited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'priority': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['beta']