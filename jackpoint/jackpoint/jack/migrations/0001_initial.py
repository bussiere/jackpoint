# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TagPrivate'
        db.create_table('jack_tagprivate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('jack', ['TagPrivate'])

        # Adding M2M table for field Tags on 'TagPrivate'
        db.create_table('jack_tagprivate_Tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tagprivate', models.ForeignKey(orm['jack.tagprivate'], null=False)),
            ('tag', models.ForeignKey(orm['tag.tag'], null=False))
        ))
        db.create_unique('jack_tagprivate_Tags', ['tagprivate_id', 'tag_id'])

        # Adding model 'ItemUser'
        db.create_table('jack_itemuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Level', self.gf('django.db.models.fields.IntegerField')()),
            ('Private', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('jack', ['ItemUser'])

        # Adding M2M table for field Item on 'ItemUser'
        db.create_table('jack_itemuser_Item', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('itemuser', models.ForeignKey(orm['jack.itemuser'], null=False)),
            ('item', models.ForeignKey(orm['item.item'], null=False))
        ))
        db.create_unique('jack_itemuser_Item', ['itemuser_id', 'item_id'])

        # Adding model 'SkillUser'
        db.create_table('jack_skilluser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Level', self.gf('django.db.models.fields.IntegerField')()),
            ('Private', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('jack', ['SkillUser'])

        # Adding M2M table for field Skills on 'SkillUser'
        db.create_table('jack_skilluser_Skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('skilluser', models.ForeignKey(orm['jack.skilluser'], null=False)),
            ('skill', models.ForeignKey(orm['skill.skill'], null=False))
        ))
        db.create_unique('jack_skilluser_Skills', ['skilluser_id', 'skill_id'])

        # Adding model 'CaracUser'
        db.create_table('jack_caracuser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Level', self.gf('django.db.models.fields.IntegerField')()),
            ('Private', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('jack', ['CaracUser'])

        # Adding M2M table for field carac on 'CaracUser'
        db.create_table('jack_caracuser_carac', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('caracuser', models.ForeignKey(orm['jack.caracuser'], null=False)),
            ('carac', models.ForeignKey(orm['carac.carac'], null=False))
        ))
        db.create_unique('jack_caracuser_carac', ['caracuser_id', 'carac_id'])

        # Adding model 'UserProfile'
        db.create_table('jack_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('Pseudo', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('Bio', self.gf('django.db.models.fields.TextField')()),
            ('Email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('Avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('Finished', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('InvitationAccepted', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='InvitationAccepted', unique=True, null=True, to=orm['invitation.Invitation'])),
        ))
        db.send_create_signal('jack', ['UserProfile'])

        # Adding M2M table for field Skills on 'UserProfile'
        db.create_table('jack_userprofile_Skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['jack.userprofile'], null=False)),
            ('skilluser', models.ForeignKey(orm['jack.skilluser'], null=False))
        ))
        db.create_unique('jack_userprofile_Skills', ['userprofile_id', 'skilluser_id'])

        # Adding M2M table for field TagsPublic on 'UserProfile'
        db.create_table('jack_userprofile_TagsPublic', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['jack.userprofile'], null=False)),
            ('tag', models.ForeignKey(orm['tag.tag'], null=False))
        ))
        db.create_unique('jack_userprofile_TagsPublic', ['userprofile_id', 'tag_id'])

        # Adding M2M table for field TagsPrivate on 'UserProfile'
        db.create_table('jack_userprofile_TagsPrivate', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['jack.userprofile'], null=False)),
            ('tagprivate', models.ForeignKey(orm['jack.tagprivate'], null=False))
        ))
        db.create_unique('jack_userprofile_TagsPrivate', ['userprofile_id', 'tagprivate_id'])

        # Adding M2M table for field Items on 'UserProfile'
        db.create_table('jack_userprofile_Items', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['jack.userprofile'], null=False)),
            ('itemuser', models.ForeignKey(orm['jack.itemuser'], null=False))
        ))
        db.create_unique('jack_userprofile_Items', ['userprofile_id', 'itemuser_id'])

        # Adding M2M table for field Caracs on 'UserProfile'
        db.create_table('jack_userprofile_Caracs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['jack.userprofile'], null=False)),
            ('caracuser', models.ForeignKey(orm['jack.caracuser'], null=False))
        ))
        db.create_unique('jack_userprofile_Caracs', ['userprofile_id', 'caracuser_id'])

        # Adding M2M table for field InvitationGiven on 'UserProfile'
        db.create_table('jack_userprofile_InvitationGiven', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['jack.userprofile'], null=False)),
            ('invitation', models.ForeignKey(orm['invitation.invitation'], null=False))
        ))
        db.create_unique('jack_userprofile_InvitationGiven', ['userprofile_id', 'invitation_id'])

    def backwards(self, orm):
        # Deleting model 'TagPrivate'
        db.delete_table('jack_tagprivate')

        # Removing M2M table for field Tags on 'TagPrivate'
        db.delete_table('jack_tagprivate_Tags')

        # Deleting model 'ItemUser'
        db.delete_table('jack_itemuser')

        # Removing M2M table for field Item on 'ItemUser'
        db.delete_table('jack_itemuser_Item')

        # Deleting model 'SkillUser'
        db.delete_table('jack_skilluser')

        # Removing M2M table for field Skills on 'SkillUser'
        db.delete_table('jack_skilluser_Skills')

        # Deleting model 'CaracUser'
        db.delete_table('jack_caracuser')

        # Removing M2M table for field carac on 'CaracUser'
        db.delete_table('jack_caracuser_carac')

        # Deleting model 'UserProfile'
        db.delete_table('jack_userprofile')

        # Removing M2M table for field Skills on 'UserProfile'
        db.delete_table('jack_userprofile_Skills')

        # Removing M2M table for field TagsPublic on 'UserProfile'
        db.delete_table('jack_userprofile_TagsPublic')

        # Removing M2M table for field TagsPrivate on 'UserProfile'
        db.delete_table('jack_userprofile_TagsPrivate')

        # Removing M2M table for field Items on 'UserProfile'
        db.delete_table('jack_userprofile_Items')

        # Removing M2M table for field Caracs on 'UserProfile'
        db.delete_table('jack_userprofile_Caracs')

        # Removing M2M table for field InvitationGiven on 'UserProfile'
        db.delete_table('jack_userprofile_InvitationGiven')

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
        'invitation.invitation': {
            'Code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Invitation'},
            'Note': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'SendTo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'Tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['invitation.Usage']", 'null': 'True', 'blank': 'True'}),
            'Used': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'invitation.usage': {
            'Meta': {'object_name': 'Usage'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        'jack.itemuser': {
            'Item': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['item.Item']", 'symmetrical': 'False'}),
            'Level': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'ItemUser'},
            'Private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jack.skilluser': {
            'Level': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'SkillUser'},
            'Private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['skill.Skill']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jack.tagprivate': {
            'Meta': {'object_name': 'TagPrivate'},
            'Tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tag.Tag']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jack.userprofile': {
            'Avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'Bio': ('django.db.models.fields.TextField', [], {}),
            'Caracs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['jack.CaracUser']", 'null': 'True', 'blank': 'True'}),
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'Finished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'InvitationAccepted': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'InvitationAccepted'", 'unique': 'True', 'null': 'True', 'to': "orm['invitation.Invitation']"}),
            'InvitationGiven': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'InvitationGiven'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['invitation.Invitation']"}),
            'Items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['jack.ItemUser']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'UserProfile'},
            'Pseudo': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['jack.SkillUser']", 'null': 'True', 'blank': 'True'}),
            'TagsPrivate': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['jack.TagPrivate']", 'null': 'True', 'blank': 'True'}),
            'TagsPublic': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tag.Tag']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
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

    complete_apps = ['jack']