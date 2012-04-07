# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table('item_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('item', ['Item'])

        # Adding M2M table for field Skills on 'Item'
        db.create_table('item_item_Skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('item', models.ForeignKey(orm['item.item'], null=False)),
            ('skill', models.ForeignKey(orm['skill.skill'], null=False))
        ))
        db.create_unique('item_item_Skills', ['item_id', 'skill_id'])

    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table('item_item')

        # Removing M2M table for field Skills on 'Item'
        db.delete_table('item_item_Skills')

    models = {
        'item.item': {
            'Meta': {'object_name': 'Item'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['skill.Skill']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'skill.skill': {
            'Child': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Child_rel_+'", 'null': 'True', 'to': "orm['skill.Skill']"}),
            'Level': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'Skill'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'Parent': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Parent_rel_+'", 'null': 'True', 'to': "orm['skill.Skill']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['item']