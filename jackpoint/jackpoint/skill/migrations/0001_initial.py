# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Skill'
        db.create_table('skill_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Level', self.gf('django.db.models.fields.IntegerField')()),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('skill', ['Skill'])

        # Adding M2M table for field Parent on 'Skill'
        db.create_table('skill_skill_Parent', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_skill', models.ForeignKey(orm['skill.skill'], null=False)),
            ('to_skill', models.ForeignKey(orm['skill.skill'], null=False))
        ))
        db.create_unique('skill_skill_Parent', ['from_skill_id', 'to_skill_id'])

        # Adding M2M table for field Child on 'Skill'
        db.create_table('skill_skill_Child', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_skill', models.ForeignKey(orm['skill.skill'], null=False)),
            ('to_skill', models.ForeignKey(orm['skill.skill'], null=False))
        ))
        db.create_unique('skill_skill_Child', ['from_skill_id', 'to_skill_id'])

    def backwards(self, orm):
        # Deleting model 'Skill'
        db.delete_table('skill_skill')

        # Removing M2M table for field Parent on 'Skill'
        db.delete_table('skill_skill_Parent')

        # Removing M2M table for field Child on 'Skill'
        db.delete_table('skill_skill_Child')

    models = {
        'skill.skill': {
            'Child': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Child_rel_+'", 'null': 'True', 'to': "orm['skill.Skill']"}),
            'Level': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'Skill'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'Parent': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Parent_rel_+'", 'null': 'True', 'to': "orm['skill.Skill']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['skill']