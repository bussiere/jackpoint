# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Answer'
        db.create_table('hand_answer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('Text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('hand', ['Answer'])

        # Adding M2M table for field Tags on 'Answer'
        db.create_table('hand_answer_Tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('answer', models.ForeignKey(orm['hand.answer'], null=False)),
            ('tag', models.ForeignKey(orm['tag.tag'], null=False))
        ))
        db.create_unique('hand_answer_Tags', ['answer_id', 'tag_id'])

        # Adding model 'Question'
        db.create_table('hand_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True, blank=True)),
            ('Text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('hand', ['Question'])

        # Adding M2M table for field Skills on 'Question'
        db.create_table('hand_question_Skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm['hand.question'], null=False)),
            ('skilluser', models.ForeignKey(orm['jack.skilluser'], null=False))
        ))
        db.create_unique('hand_question_Skills', ['question_id', 'skilluser_id'])

        # Adding M2M table for field Tags on 'Question'
        db.create_table('hand_question_Tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm['hand.question'], null=False)),
            ('tag', models.ForeignKey(orm['tag.tag'], null=False))
        ))
        db.create_unique('hand_question_Tags', ['question_id', 'tag_id'])

        # Adding M2M table for field Items on 'Question'
        db.create_table('hand_question_Items', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm['hand.question'], null=False)),
            ('item', models.ForeignKey(orm['item.item'], null=False))
        ))
        db.create_unique('hand_question_Items', ['question_id', 'item_id'])

        # Adding M2M table for field Caracs on 'Question'
        db.create_table('hand_question_Caracs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm['hand.question'], null=False)),
            ('caracuser', models.ForeignKey(orm['jack.caracuser'], null=False))
        ))
        db.create_unique('hand_question_Caracs', ['question_id', 'caracuser_id'])

    def backwards(self, orm):
        # Deleting model 'Answer'
        db.delete_table('hand_answer')

        # Removing M2M table for field Tags on 'Answer'
        db.delete_table('hand_answer_Tags')

        # Deleting model 'Question'
        db.delete_table('hand_question')

        # Removing M2M table for field Skills on 'Question'
        db.delete_table('hand_question_Skills')

        # Removing M2M table for field Tags on 'Question'
        db.delete_table('hand_question_Tags')

        # Removing M2M table for field Items on 'Question'
        db.delete_table('hand_question_Items')

        # Removing M2M table for field Caracs on 'Question'
        db.delete_table('hand_question_Caracs')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'carac.carac': {
            'Commentaire': ('django.db.models.fields.TextField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Carac'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hand.answer': {
            'Meta': {'object_name': 'Answer'},
            'Tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tag.Tag']", 'null': 'True', 'blank': 'True'}),
            'Text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'hand.question': {
            'Caracs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['jack.CaracUser']", 'null': 'True', 'blank': 'True'}),
            'Items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['item.Item']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Question'},
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['jack.SkillUser']", 'null': 'True', 'blank': 'True'}),
            'Tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tag.Tag']", 'null': 'True', 'blank': 'True'}),
            'Text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'item.item': {
            'Meta': {'object_name': 'Item'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['skill.Skill']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jack.caracuser': {
            'Level': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'CaracUser'},
            'Private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'carac': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['carac.Carac']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jack.skilluser': {
            'Level': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'SkillUser'},
            'Private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        },
        'tag.tag': {
            'Meta': {'object_name': 'Tag'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['hand']