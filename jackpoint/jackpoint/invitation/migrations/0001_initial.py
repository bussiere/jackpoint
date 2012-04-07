# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Task'
        db.create_table('invitation_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('invitation', ['Task'])

        # Adding model 'CategorieInvitation'
        db.create_table('invitation_categorieinvitation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal('invitation', ['CategorieInvitation'])

        # Adding model 'Usage'
        db.create_table('invitation_usage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
        ))
        db.send_create_signal('invitation', ['Usage'])

        # Adding model 'Invitation'
        db.create_table('invitation_invitation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Code', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('Note', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('Used', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('SendTo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('invitation', ['Invitation'])

        # Adding M2M table for field Tags on 'Invitation'
        db.create_table('invitation_invitation_Tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('invitation', models.ForeignKey(orm['invitation.invitation'], null=False)),
            ('usage', models.ForeignKey(orm['invitation.usage'], null=False))
        ))
        db.create_unique('invitation_invitation_Tags', ['invitation_id', 'usage_id'])

        # Adding model 'InvitationUsed'
        db.create_table('invitation_invitationused', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Code', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('Note', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('SendTo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('invitation', ['InvitationUsed'])

        # Adding M2M table for field Tags on 'InvitationUsed'
        db.create_table('invitation_invitationused_Tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('invitationused', models.ForeignKey(orm['invitation.invitationused'], null=False)),
            ('usage', models.ForeignKey(orm['invitation.usage'], null=False))
        ))
        db.create_unique('invitation_invitationused_Tags', ['invitationused_id', 'usage_id'])

        # Adding M2M table for field Receveur on 'InvitationUsed'
        db.create_table('invitation_invitationused_Receveur', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('invitationused', models.ForeignKey(orm['invitation.invitationused'], null=False)),
            ('userprofile', models.ForeignKey(orm['jack.userprofile'], null=False))
        ))
        db.create_unique('invitation_invitationused_Receveur', ['invitationused_id', 'userprofile_id'])

        # Adding M2M table for field Donneur on 'InvitationUsed'
        db.create_table('invitation_invitationused_Donneur', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('invitationused', models.ForeignKey(orm['invitation.invitationused'], null=False)),
            ('userprofile', models.ForeignKey(orm['jack.userprofile'], null=False))
        ))
        db.create_unique('invitation_invitationused_Donneur', ['invitationused_id', 'userprofile_id'])

    def backwards(self, orm):
        # Deleting model 'Task'
        db.delete_table('invitation_task')

        # Deleting model 'CategorieInvitation'
        db.delete_table('invitation_categorieinvitation')

        # Deleting model 'Usage'
        db.delete_table('invitation_usage')

        # Deleting model 'Invitation'
        db.delete_table('invitation_invitation')

        # Removing M2M table for field Tags on 'Invitation'
        db.delete_table('invitation_invitation_Tags')

        # Deleting model 'InvitationUsed'
        db.delete_table('invitation_invitationused')

        # Removing M2M table for field Tags on 'InvitationUsed'
        db.delete_table('invitation_invitationused_Tags')

        # Removing M2M table for field Receveur on 'InvitationUsed'
        db.delete_table('invitation_invitationused_Receveur')

        # Removing M2M table for field Donneur on 'InvitationUsed'
        db.delete_table('invitation_invitationused_Donneur')

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
        'invitation.categorieinvitation': {
            'Meta': {'object_name': 'CategorieInvitation'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        'invitation.invitationused': {
            'Code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'Donneur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'DonneurINvit'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['jack.UserProfile']"}),
            'Meta': {'object_name': 'InvitationUsed'},
            'Note': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'Receveur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'ReceveurINvit'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['jack.UserProfile']"}),
            'SendTo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'Tags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['invitation.Usage']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'invitation.task': {
            'Meta': {'object_name': 'Task'},
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

    complete_apps = ['invitation']