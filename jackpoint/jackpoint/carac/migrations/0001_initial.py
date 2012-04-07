# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carac'
        db.create_table('carac_carac', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('Commentaire', self.gf('django.db.models.fields.TextField')(max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('carac', ['Carac'])

    def backwards(self, orm):
        # Deleting model 'Carac'
        db.delete_table('carac_carac')

    models = {
        'carac.carac': {
            'Commentaire': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Carac'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['carac']