# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Date_Visite'
        db.create_table('membre_date_visite', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('membre', ['Date_Visite'])

        # Adding model 'Site_hack_css'
        db.create_table('membre_site_hack_css', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Site', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('membre', ['Site_hack_css'])

        # Adding model 'Anonymous'
        db.create_table('membre_anonymous', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Referer', self.gf('django.db.models.fields.CharField')(max_length=1500)),
        ))
        db.send_create_signal('membre', ['Anonymous'])

        # Adding M2M table for field Langue on 'Anonymous'
        db.create_table('membre_anonymous_Langue', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('anonymous', models.ForeignKey(orm['membre.anonymous'], null=False)),
            ('langue', models.ForeignKey(orm['presentation.langue'], null=False))
        ))
        db.create_unique('membre_anonymous_Langue', ['anonymous_id', 'langue_id'])

        # Adding M2M table for field IP on 'Anonymous'
        db.create_table('membre_anonymous_IP', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('anonymous', models.ForeignKey(orm['membre.anonymous'], null=False)),
            ('ip', models.ForeignKey(orm['ip.ip'], null=False))
        ))
        db.create_unique('membre_anonymous_IP', ['anonymous_id', 'ip_id'])

        # Adding M2M table for field Date_Visite on 'Anonymous'
        db.create_table('membre_anonymous_Date_Visite', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('anonymous', models.ForeignKey(orm['membre.anonymous'], null=False)),
            ('date_visite', models.ForeignKey(orm['membre.date_visite'], null=False))
        ))
        db.create_unique('membre_anonymous_Date_Visite', ['anonymous_id', 'date_visite_id'])

        # Adding model 'Signature'
        db.create_table('membre_signature', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Texte', self.gf('django.db.models.fields.CharField')(max_length=450)),
        ))
        db.send_create_signal('membre', ['Signature'])

        # Adding model 'Skill_user'
        db.create_table('membre_skill_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Niveau', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
        ))
        db.send_create_signal('membre', ['Skill_user'])

        # Adding M2M table for field Skills on 'Skill_user'
        db.create_table('membre_skill_user_Skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('skill_user', models.ForeignKey(orm['membre.skill_user'], null=False)),
            ('skill', models.ForeignKey(orm['skill.skill'], null=False))
        ))
        db.create_unique('membre_skill_user_Skills', ['skill_user_id', 'skill_id'])

        # Adding model 'Membre'
        db.create_table('membre_membre', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('User', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('Nom', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Prenom', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Date_inscription', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Naissance', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('Referer', self.gf('django.db.models.fields.CharField')(max_length=1500, null=True, blank=True)),
            ('Abo_Newsletter', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('membre', ['Membre'])

        # Adding M2M table for field Email on 'Membre'
        db.create_table('membre_membre_Email', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('email', models.ForeignKey(orm['contact.email'], null=False))
        ))
        db.create_unique('membre_membre_Email', ['membre_id', 'email_id'])

        # Adding M2M table for field Tel on 'Membre'
        db.create_table('membre_membre_Tel', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('telephone', models.ForeignKey(orm['contact.telephone'], null=False))
        ))
        db.create_unique('membre_membre_Tel', ['membre_id', 'telephone_id'])

        # Adding M2M table for field Tag on 'Membre'
        db.create_table('membre_membre_Tag', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('tag', models.ForeignKey(orm['tag.tag'], null=False))
        ))
        db.create_unique('membre_membre_Tag', ['membre_id', 'tag_id'])

        # Adding M2M table for field IP on 'Membre'
        db.create_table('membre_membre_IP', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('ip', models.ForeignKey(orm['ip.ip'], null=False))
        ))
        db.create_unique('membre_membre_IP', ['membre_id', 'ip_id'])

        # Adding M2M table for field Note_divers on 'Membre'
        db.create_table('membre_membre_Note_divers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('note_divers', models.ForeignKey(orm['note.note_divers'], null=False))
        ))
        db.create_unique('membre_membre_Note_divers', ['membre_id', 'note_divers_id'])

        # Adding M2M table for field Langue on 'Membre'
        db.create_table('membre_membre_Langue', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('langue', models.ForeignKey(orm['presentation.langue'], null=False))
        ))
        db.create_unique('membre_membre_Langue', ['membre_id', 'langue_id'])

        # Adding M2M table for field Date_Visite on 'Membre'
        db.create_table('membre_membre_Date_Visite', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('date_visite', models.ForeignKey(orm['membre.date_visite'], null=False))
        ))
        db.create_unique('membre_membre_Date_Visite', ['membre_id', 'date_visite_id'])

        # Adding M2M table for field Was_Anonymous on 'Membre'
        db.create_table('membre_membre_Was_Anonymous', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('anonymous', models.ForeignKey(orm['anonymous.anonymous'], null=False))
        ))
        db.create_unique('membre_membre_Was_Anonymous', ['membre_id', 'anonymous_id'])

        # Adding M2M table for field Categorie on 'Membre'
        db.create_table('membre_membre_Categorie', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('categorie_membre', models.ForeignKey(orm['configurationsite.categorie_membre'], null=False))
        ))
        db.create_unique('membre_membre_Categorie', ['membre_id', 'categorie_membre_id'])

        # Adding M2M table for field Historique_hack_css on 'Membre'
        db.create_table('membre_membre_Historique_hack_css', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('site_hack_css', models.ForeignKey(orm['membre.site_hack_css'], null=False))
        ))
        db.create_unique('membre_membre_Historique_hack_css', ['membre_id', 'site_hack_css_id'])

        # Adding M2M table for field Skills on 'Membre'
        db.create_table('membre_membre_Skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('skill_user', models.ForeignKey(orm['membre.skill_user'], null=False))
        ))
        db.create_unique('membre_membre_Skills', ['membre_id', 'skill_user_id'])

        # Adding M2M table for field Lieux on 'Membre'
        db.create_table('membre_membre_Lieux', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('lieux', models.ForeignKey(orm['lieux.lieux'], null=False))
        ))
        db.create_unique('membre_membre_Lieux', ['membre_id', 'lieux_id'])

        # Adding M2M table for field Fiche on 'Membre'
        db.create_table('membre_membre_Fiche', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('fiche', models.ForeignKey(orm['fiche.fiche'], null=False))
        ))
        db.create_unique('membre_membre_Fiche', ['membre_id', 'fiche_id'])

        # Adding M2M table for field Gallery on 'Membre'
        db.create_table('membre_membre_Gallery', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('gallerie', models.ForeignKey(orm['gallerie.gallerie'], null=False))
        ))
        db.create_unique('membre_membre_Gallery', ['membre_id', 'gallerie_id'])

        # Adding M2M table for field Liens on 'Membre'
        db.create_table('membre_membre_Liens', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('lien', models.ForeignKey(orm['lien.lien'], null=False))
        ))
        db.create_unique('membre_membre_Liens', ['membre_id', 'lien_id'])

        # Adding M2M table for field LienFacebook on 'Membre'
        db.create_table('membre_membre_LienFacebook', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('lienfacebook', models.ForeignKey(orm['lien.lienfacebook'], null=False))
        ))
        db.create_unique('membre_membre_LienFacebook', ['membre_id', 'lienfacebook_id'])

        # Adding M2M table for field LienTwitter on 'Membre'
        db.create_table('membre_membre_LienTwitter', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('lientwitter', models.ForeignKey(orm['lien.lientwitter'], null=False))
        ))
        db.create_unique('membre_membre_LienTwitter', ['membre_id', 'lientwitter_id'])

        # Adding M2M table for field Signature on 'Membre'
        db.create_table('membre_membre_Signature', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('signature', models.ForeignKey(orm['membre.signature'], null=False))
        ))
        db.create_unique('membre_membre_Signature', ['membre_id', 'signature_id'])

        # Adding M2M table for field Jugement on 'Membre'
        db.create_table('membre_membre_Jugement', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('jugement', models.ForeignKey(orm['jugement.jugement'], null=False))
        ))
        db.create_unique('membre_membre_Jugement', ['membre_id', 'jugement_id'])

        # Adding M2M table for field PoigneeMain on 'Membre'
        db.create_table('membre_membre_PoigneeMain', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('poignee', models.ForeignKey(orm['poigneemain.poignee'], null=False))
        ))
        db.create_unique('membre_membre_PoigneeMain', ['membre_id', 'poignee_id'])

        # Adding M2M table for field Kharma on 'Membre'
        db.create_table('membre_membre_Kharma', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('kharma', models.ForeignKey(orm['kharma.kharma'], null=False))
        ))
        db.create_unique('membre_membre_Kharma', ['membre_id', 'kharma_id'])

        # Adding M2M table for field Importance on 'Membre'
        db.create_table('membre_membre_Importance', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('importance', models.ForeignKey(orm['importance.importance'], null=False))
        ))
        db.create_unique('membre_membre_Importance', ['membre_id', 'importance_id'])

        # Adding M2M table for field Reputation on 'Membre'
        db.create_table('membre_membre_Reputation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False)),
            ('reputation', models.ForeignKey(orm['reputation.reputation'], null=False))
        ))
        db.create_unique('membre_membre_Reputation', ['membre_id', 'reputation_id'])

        # Adding model 'liste'
        db.create_table('membre_liste', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('membre', ['liste'])

        # Adding M2M table for field Membre on 'liste'
        db.create_table('membre_liste_Membre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('liste', models.ForeignKey(orm['membre.liste'], null=False)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False))
        ))
        db.create_unique('membre_liste_Membre', ['liste_id', 'membre_id'])

        # Adding M2M table for field Amis on 'liste'
        db.create_table('membre_liste_Amis', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('liste', models.ForeignKey(orm['membre.liste'], null=False)),
            ('membre', models.ForeignKey(orm['membre.membre'], null=False))
        ))
        db.create_unique('membre_liste_Amis', ['liste_id', 'membre_id'])


    def backwards(self, orm):
        
        # Deleting model 'Date_Visite'
        db.delete_table('membre_date_visite')

        # Deleting model 'Site_hack_css'
        db.delete_table('membre_site_hack_css')

        # Deleting model 'Anonymous'
        db.delete_table('membre_anonymous')

        # Removing M2M table for field Langue on 'Anonymous'
        db.delete_table('membre_anonymous_Langue')

        # Removing M2M table for field IP on 'Anonymous'
        db.delete_table('membre_anonymous_IP')

        # Removing M2M table for field Date_Visite on 'Anonymous'
        db.delete_table('membre_anonymous_Date_Visite')

        # Deleting model 'Signature'
        db.delete_table('membre_signature')

        # Deleting model 'Skill_user'
        db.delete_table('membre_skill_user')

        # Removing M2M table for field Skills on 'Skill_user'
        db.delete_table('membre_skill_user_Skills')

        # Deleting model 'Membre'
        db.delete_table('membre_membre')

        # Removing M2M table for field Email on 'Membre'
        db.delete_table('membre_membre_Email')

        # Removing M2M table for field Tel on 'Membre'
        db.delete_table('membre_membre_Tel')

        # Removing M2M table for field Tag on 'Membre'
        db.delete_table('membre_membre_Tag')

        # Removing M2M table for field IP on 'Membre'
        db.delete_table('membre_membre_IP')

        # Removing M2M table for field Note_divers on 'Membre'
        db.delete_table('membre_membre_Note_divers')

        # Removing M2M table for field Langue on 'Membre'
        db.delete_table('membre_membre_Langue')

        # Removing M2M table for field Date_Visite on 'Membre'
        db.delete_table('membre_membre_Date_Visite')

        # Removing M2M table for field Was_Anonymous on 'Membre'
        db.delete_table('membre_membre_Was_Anonymous')

        # Removing M2M table for field Categorie on 'Membre'
        db.delete_table('membre_membre_Categorie')

        # Removing M2M table for field Historique_hack_css on 'Membre'
        db.delete_table('membre_membre_Historique_hack_css')

        # Removing M2M table for field Skills on 'Membre'
        db.delete_table('membre_membre_Skills')

        # Removing M2M table for field Lieux on 'Membre'
        db.delete_table('membre_membre_Lieux')

        # Removing M2M table for field Fiche on 'Membre'
        db.delete_table('membre_membre_Fiche')

        # Removing M2M table for field Gallery on 'Membre'
        db.delete_table('membre_membre_Gallery')

        # Removing M2M table for field Liens on 'Membre'
        db.delete_table('membre_membre_Liens')

        # Removing M2M table for field LienFacebook on 'Membre'
        db.delete_table('membre_membre_LienFacebook')

        # Removing M2M table for field LienTwitter on 'Membre'
        db.delete_table('membre_membre_LienTwitter')

        # Removing M2M table for field Signature on 'Membre'
        db.delete_table('membre_membre_Signature')

        # Removing M2M table for field Jugement on 'Membre'
        db.delete_table('membre_membre_Jugement')

        # Removing M2M table for field PoigneeMain on 'Membre'
        db.delete_table('membre_membre_PoigneeMain')

        # Removing M2M table for field Kharma on 'Membre'
        db.delete_table('membre_membre_Kharma')

        # Removing M2M table for field Importance on 'Membre'
        db.delete_table('membre_membre_Importance')

        # Removing M2M table for field Reputation on 'Membre'
        db.delete_table('membre_membre_Reputation')

        # Deleting model 'liste'
        db.delete_table('membre_liste')

        # Removing M2M table for field Membre on 'liste'
        db.delete_table('membre_liste_Membre')

        # Removing M2M table for field Amis on 'liste'
        db.delete_table('membre_liste_Amis')


    models = {
        'anonymous.anonymous': {
            'Meta': {'object_name': 'Anonymous'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'article.article': {
            'Groupe': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'GroupeCreateur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'GroupeCreateur_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'GroupeReco': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'GroupeReco_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'Membre': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'MembreCreateur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MembreCreateur_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'MembreReco': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MembreReco_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'Meta': {'object_name': 'Article'},
            'Notation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Notation_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['notation.Notation']"}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Skills_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['skill.Skill']"}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Article_Tag'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Texte': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['article.Texte_Article']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'article.categorietexte': {
            'Meta': {'object_name': 'CategorieTexte'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Visibilite_CategorieTexte'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'article.texte_article': {
            'CategorieTexte': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['article.CategorieTexte']", 'null': 'True', 'blank': 'True'}),
            'Date': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Date_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['date.Date']"}),
            'Evenement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['evenement.Evenement']"}),
            'Image': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['image.Image']"}),
            'Info': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['info.Info']"}),
            'Lien': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lien_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'LienFacebook': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'LienFacebook_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienFacebook']"}),
            'LienTwitter': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'LienTwitter_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienTwitter']"}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lieux_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'Meta': {'object_name': 'Texte_Article'},
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Article_Tag_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '100000'}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Visibilite_Texte_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
        'configurationsite.categorie_membre': {
            'Meta': {'object_name': 'Categorie_Membre'},
            'Nom': ('django.db.models.fields.IntegerField', [], {'max_length': '200', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'Categorie_Membre_Note_divers_notes_Note_divers'", 'blank': 'True', 'to': "orm['note.Note_divers']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contact.email': {
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'Meta': {'object_name': 'Email'},
            'Principal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contact.telephone': {
            'Meta': {'object_name': 'Telephone'},
            'Principal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'date.date': {
            'Date': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Meta': {'object_name': 'Date'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'evenement.evenement': {
            'Date_Evenement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Date_Evenement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['date.Date']"}),
            'Date_inscription': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Email': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Email_contact_Email'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['contact.Email']"}),
            'Fiche': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fiche.Fiche']", 'null': 'True', 'blank': 'True'}),
            'Gallery': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['gallerie.Gallerie']", 'null': 'True', 'blank': 'True'}),
            'Importance': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Importance_importance_Importance'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['importance.Importance']"}),
            'Jugement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Jugement_jugement_Jugement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['jugement.Jugement']"}),
            'Kharma': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Kharma_kharma_Kharma'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['kharma.Kharma']"}),
            'LienFacebook': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_LienFacebook_liens_LienFacebook'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienFacebook']"}),
            'LienTwitter': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_LienTwitter_liens_LienTwitter'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienTwitter']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Liens_liens_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Lieux_lieux_Lieux)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'Meta': {'object_name': 'Evenement'},
            'Naissance': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Note_divers_note_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'Reputation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Reputation_reputation_Reputation'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['reputation.Reputation']"}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Skills_skills_Skills)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['skill.Skill']"}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Tag_tag_Tag'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Tel': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Evenement_Tel_contact_Telephone'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['contact.Telephone']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'fiche.categorietexte': {
            'Meta': {'object_name': 'CategorieTexte'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Fiche_Categorie_Texte_Visibilite_Visibilite_visibilite'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'fiche.entete': {
            'Meta': {'object_name': 'Entete'},
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'fiche.fiche': {
            'Entete': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fiche.Entete']", 'null': 'True', 'blank': 'True'}),
            'Gallerie': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Fiche_Fiche_Gallerie_gallerie_Gallerie'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['gallerie.Gallerie']"}),
            'Meta': {'object_name': 'Fiche'},
            'Texte': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fiche.Texte']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'fiche.texte': {
            'CategorieTexte': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fiche.CategorieTexte']", 'null': 'True', 'blank': 'True'}),
            'Date': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Fiche_Texte_Date_date_Date'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['date.Date']"}),
            'Evenement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Fiche_Texte_Evenement_evenement_Evenement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['evenement.Evenement']"}),
            'Image': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Fiche_Texte_Image_image_image'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['image.Image']"}),
            'Lien': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Fiche_Texte_Lien_lien_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Fiche_Texte_Lieux_lieux_Lieux'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'Meta': {'object_name': 'Texte'},
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Fiche_Texte_Tag_tag_Tags'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Fiche_Texte_Visibilite_Visibilite_visibilite'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'gallerie.gallerie': {
            'CategorieGallerie': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Date': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Gallerie_Date_date_Date'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['date.Date']"}),
            'Evenement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Gallerie_Evenement_evenement_Evenement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['evenement.Evenement']"}),
            'Image': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Gallerie_Image_image_image'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['image.Image']"}),
            'Lien': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Gallerie_Lien_lien_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Gallerie_Lieux_lieux_Lieux'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'Meta': {'object_name': 'Gallerie'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Gallerie_Tag_tag_Tags'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Gallerie_Visibilite_Visibilite_visibilite'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'groupe.date_visite': {
            'Date': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Date_Visite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'groupe.groupe': {
            'Abo_Newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Date_Visite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['groupe.Date_Visite']", 'null': 'True', 'blank': 'True'}),
            'Date_creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Fiche': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fiche.Fiche']", 'null': 'True', 'blank': 'True'}),
            'Gallery': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['gallerie.Gallerie']", 'null': 'True', 'blank': 'True'}),
            'IP': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_IP_ip_IP'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['ip.IP']"}),
            'Importance': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Importance_importance_Importance'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['importance.Importance']"}),
            'Jugement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Jugement_jugement_Jugement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['jugement.Jugement']"}),
            'Kharma': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Kharma_kharma_Kharma'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['kharma.Kharma']"}),
            'Langue': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Langue_langue_Langue'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['langue.Langue']"}),
            'LienFacebook': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_LienFacebook_liens_LienFacebook'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienFacebook']"}),
            'LienTwitter': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_LienTwitter_liens_LienTwitter'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienTwitter']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Liens_liens_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Lieux_lieux_Lieux)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'Membre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['membre.Membre']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'Groupe'},
            'Naissance': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Note_divers_note_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'PoigneeMain': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_PoigneeMain_poigneemain_PoigneeMain'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['poigneemain.Poignee']"}),
            'Referer': ('django.db.models.fields.CharField', [], {'max_length': '1500', 'null': 'True', 'blank': 'True'}),
            'Reputation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Reputation_reputation_Reputation'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['reputation.Reputation']"}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Skills_skills_Skills)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['skill.Skill']"}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Groupe_Tag_tag_Tag'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'horaire.horaire': {
            'HoraireDebut': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['horaire.HoraireDebut']", 'null': 'True', 'blank': 'True'}),
            'HoraireFin': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['horaire.HoraireFin']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Horaire'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'horaire.horairedebut': {
            'Heure': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'Meta': {'object_name': 'HoraireDebut'},
            'Minute': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'horaire.horairefin': {
            'Heure': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'Meta': {'object_name': 'HoraireFin'},
            'Minute': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'image.image': {
            'Anonymous': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Anonymous_anonymous_anonymous'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['anonymous.Anonymous']"}),
            'Base64': ('django.db.models.fields.CharField', [], {'max_length': '1000000'}),
            'Date': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Date_date_Date'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['date.Date']"}),
            'Evenement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Evenement_evenement_Evenement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['evenement.Evenement']"}),
            'Groupe': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Groupe_groupe_groupe'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'Lien': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Lien_lien_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Lieux_lieux_Lieux'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'Membre': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Membre_membre_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'Meta': {'object_name': 'Image'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'Projet': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Projet_projet_projet'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['projet.Projet']"}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Tag_tag_tag'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Image_Visibilite_Visibilite_visibilite'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'importance.importance': {
            'Importance': ('django.db.models.fields.FloatField', [], {'max_length': '1000'}),
            'Meta': {'object_name': 'Importance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'info.info': {
            'Fiche': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fiche.Fiche']", 'null': 'True', 'blank': 'True'}),
            'Groupe': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_Groupe_groupe_Groupe'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'GroupeCreateur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_GroupeCreateur_groupe_Groupe'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'GroupeReco': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_GroupeReco_groupe_Groupe'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'LienFacebook': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_LienFacebook_liens_LienFacebook'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienFacebook']"}),
            'LienTwitter': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_LienTwitter_liens_LienTwitter'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienTwitter']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_Liens_liens_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_Lieux_lieux_Lieux)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'MembreCreateur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_MembreCreateur_membre_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'Membrevise': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_Membrevise_membre_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'Meta': {'object_name': 'Info'},
            'Personne': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_Personne_personne_Personne'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['personne.Personne']"}),
            'PersonneGroupe': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_PersonneGroupe_personnegroupe_PersonneGroupe'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['personnegroupe.PersonneGroupe']"}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_Skills_skills_Skills'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['skill.Skill']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membreReco': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Info_Info_membreReco_membre_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"})
        },
        'ip.ip': {
            'Meta': {'object_name': 'IP'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'jugement.jugement': {
            'Date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Dest': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Jugement_Dest'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'Meta': {'object_name': 'Jugement'},
            'NoteBoulet': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jugement.NoteBoulet']", 'symmetrical': 'False'}),
            'NoteDangerosite': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['jugement.NoteDangerosite']", 'symmetrical': 'False'}),
            'Object': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'Sender': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Jugement_Sender'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '1500'}),
            'Visiblite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jugement.noteboulet': {
            'Meta': {'object_name': 'NoteBoulet'},
            'NoteBoulet': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'jugement.notedangerosite': {
            'Meta': {'object_name': 'NoteDangerosite'},
            'NoteDangerosite': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'kharma.kharma': {
            'Kharma': ('django.db.models.fields.FloatField', [], {'max_length': '1000'}),
            'Meta': {'object_name': 'Kharma'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'langue.langue': {
            'Abr': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'Meta': {'object_name': 'Langue'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Langue_Note_divers_notes_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lien.categorielien': {
            'Meta': {'object_name': 'CategorieLien'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Categorie_Lien_Note_divers_notes_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Categorie_Lien_Visibilite_Visibilite'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lien.lien': {
            'Categorie': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lien.CategorieLien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Lien'},
            'MiseEnForme': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lien_MiseEnForme_presentation_MiseEnForme'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['presentation.MiseEnForme']"}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lien_Note_divers_notes_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'Texte_contenu': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lien_Texte_contenu_presentation_Texte_contenu'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['presentation.Texte_contenu']"}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lien_Visibilite_Visibilite'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']"}),
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'lien.lienfacebook': {
            'LienFacaebook': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lien.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'LienFacebook'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lien.lientwitter': {
            'LienTwitter': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lien.Lien']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'LienTwitter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'lieux.lieux': {
            'Horaire': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lieux_Horaire'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['horaire.Horaire']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lieux_Liens_liens_Lien'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Localisation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lieux_Localisation_localisation_localisation'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['localisation.Localisation']"}),
            'Meta': {'object_name': 'Lieux'},
            'Notation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lieux_Notation_Notation_notation'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['notation.Notation']"}),
            'Note': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lieux_Note_notes_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'Tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Lieux_Tags'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'localisation.adresse': {
            'GPS': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GeoHash': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GoogleMaps': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Adresse_Google'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Adresse_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Meta': {'object_name': 'Adresse'},
            'Nom': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localisation.NomsEndroit']", 'symmetrical': 'False'}),
            'Numero': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'localisation.etat': {
            'GPS': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GeoHash': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GoogleMaps': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Etat_Google'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Etat_liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Meta': {'object_name': 'Etat'},
            'Nom': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localisation.NomsEndroit']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'localisation.localisation': {
            'Adresse': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Localisation_Adresse'", 'symmetrical': 'False', 'to': "orm['localisation.Adresse']"}),
            'GPS': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GeoHash': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GoogleMaps': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Localisation_GoogleMaps'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Localisation_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Meta': {'object_name': 'Localisation'},
            'Tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Localisation_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'etat': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localisation.Etat']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pays': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localisation.Pays']", 'symmetrical': 'False'}),
            'region': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localisation.Region']", 'symmetrical': 'False'}),
            'ville': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Localisation_Ville'", 'symmetrical': 'False', 'to': "orm['localisation.Ville']"})
        },
        'localisation.nomsendroit': {
            'Meta': {'object_name': 'NomsEndroit'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'localisation.pays': {
            'GPS': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GeoHash': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GoogleMaps': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Pays_Google'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Pays_liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Meta': {'object_name': 'Pays'},
            'Nom': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localisation.NomsEndroit']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'localisation.region': {
            'GPS': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GeoHash': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GoogleMaps': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Region_Google'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Region_liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Meta': {'object_name': 'Region'},
            'Nom': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localisation.NomsEndroit']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'localisation.ville': {
            'GPS': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GeoHash': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'GoogleMaps': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Ville_Google'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Ville_liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Meta': {'object_name': 'Ville'},
            'Nom': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localisation.NomsEndroit']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'membre.anonymous': {
            'Date_Visite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['membre.Date_Visite']", 'null': 'True', 'blank': 'True'}),
            'IP': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ip.IP']", 'symmetrical': 'False'}),
            'Langue': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['presentation.Langue']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'Anonymous'},
            'Referer': ('django.db.models.fields.CharField', [], {'max_length': '1500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'membre.date_visite': {
            'Date': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Date_Visite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'membre.liste': {
            'Amis': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Amis_membre_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'Membre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['membre.Membre']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'liste'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'membre.membre': {
            'Abo_Newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Categorie': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Categorie_configuration_Categorie_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['configurationsite.Categorie_Membre']"}),
            'Date_Visite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['membre.Date_Visite']", 'null': 'True', 'blank': 'True'}),
            'Date_inscription': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Email': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Email_contact_Email'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['contact.Email']"}),
            'Fiche': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fiche.Fiche']", 'null': 'True', 'blank': 'True'}),
            'Gallery': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['gallerie.Gallerie']", 'null': 'True', 'blank': 'True'}),
            'Historique_hack_css': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['membre.Site_hack_css']", 'null': 'True', 'blank': 'True'}),
            'IP': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_IP_ip_IP'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['ip.IP']"}),
            'Importance': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Importance_importance_Importance'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['importance.Importance']"}),
            'Jugement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Jugement_jugement_Jugement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['jugement.Jugement']"}),
            'Kharma': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Kharma_kharma_Kharma'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['kharma.Kharma']"}),
            'Langue': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Langue']", 'null': 'True', 'blank': 'True'}),
            'LienFacebook': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_LienFacebook_liens_LienFacebook'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienFacebook']"}),
            'LienTwitter': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_LienTwitter_liens_LienTwitter'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienTwitter']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Liens_liens_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Lieux_lieux_Lieux)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'Meta': {'object_name': 'Membre'},
            'Naissance': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Note_divers_note_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'PoigneeMain': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_PoigneeMain_poigneemain_PoigneeMain'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['poigneemain.Poignee']"}),
            'Prenom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Referer': ('django.db.models.fields.CharField', [], {'max_length': '1500', 'null': 'True', 'blank': 'True'}),
            'Reputation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Reputation_reputation_Reputation'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['reputation.Reputation']"}),
            'Signature': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['membre.Signature']", 'symmetrical': 'False'}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Skills_skills_Skills)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Skill_user']"}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Tag_tag_Tag'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Tel': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Tel_contact_Telephone'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['contact.Telephone']"}),
            'User': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'Was_Anonymous': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anonymous.Anonymous']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'membre.signature': {
            'Meta': {'object_name': 'Signature'},
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '450'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'membre.site_hack_css': {
            'Meta': {'object_name': 'Site_hack_css'},
            'Site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'membre.skill_user': {
            'Meta': {'object_name': 'Skill_user'},
            'Niveau': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Membre_Skills_skills_Skills)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['skill.Skill']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'notation.notation': {
            'Membre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['membre.Membre']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'Notation'},
            'Notation': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'note.categorie_note': {
            'Meta': {'object_name': 'Categorie_Note'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'note.note_divers': {
            'Categorie': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['note.Categorie_Note']", 'symmetrical': 'False'}),
            'Geohash': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Lien': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['lien.Lien']", 'null': 'True', 'blank': 'True'}),
            'Membre': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['membre.Membre']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Note_divers'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'Tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tag.Tag']", 'symmetrical': 'False'}),
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'personne.personne': {
            'Date_inscription': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'Fiche': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fiche.Fiche']", 'symmetrical': 'False'}),
            'Gallery': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['gallerie.Gallerie']", 'symmetrical': 'False'}),
            'GroupeCreateur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_GroupeCreateur_groupe_Groupe'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'IP': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_IP_ip_IP'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['ip.IP']"}),
            'Immatriculation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Importance': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_Importance_importance_Importance'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['importance.Importance']"}),
            'Jugement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_Jugement_jugement_Jugement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['jugement.Jugement']"}),
            'Kharma': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_Kharma_kharma_Kharma'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['kharma.Kharma']"}),
            'LienFacebook': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lien.LienFacebook']", 'symmetrical': 'False'}),
            'LienTwitter': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lien.LienTwitter']", 'symmetrical': 'False'}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lien.Lien']", 'symmetrical': 'False'}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_Lieux_lieux_Lieux)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'MembreCreateur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_MembreCreateur_membre_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'Meta': {'object_name': 'Personne'},
            'Naissance': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_Note_divers_note_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'Portable': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Prenom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Reputation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_Reputation_reputation_Reputation'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['reputation.Reputation']"}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_Skills_skills_Skills)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['skill.Skill']"}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Personne_Tag_tag_Tag'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Telephone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'personnegroupe.personnegroupe': {
            'Date_inscription': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'Fiche': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fiche.Fiche']", 'symmetrical': 'False'}),
            'Gallery': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['gallerie.Gallerie']", 'symmetrical': 'False'}),
            'GroupeCreateur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_GroupeCreateur_groupe_Groupe'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'IP': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_IP_ip_IP'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['ip.IP']"}),
            'Importance': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_Importance_importance_Importance'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['importance.Importance']"}),
            'Jugement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_Jugement_jugement_Jugement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['jugement.Jugement']"}),
            'Kharma': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_Kharma_kharma_Kharma'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['kharma.Kharma']"}),
            'LienFacebook': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lien.LienFacebook']", 'symmetrical': 'False'}),
            'LienTwitter': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lien.LienTwitter']", 'symmetrical': 'False'}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lien.Lien']", 'symmetrical': 'False'}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_Lieux_lieux_Lieux)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'MembreCreateur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_MembreCreateur_membre_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'Meta': {'object_name': 'PersonneGroupe'},
            'Naissance': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_Note_divers_note_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'Personne': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_Personne_personne_Personne'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['personne.Personne']"}),
            'Portable': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Prenom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Reputation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_Reputation_reputation_Reputation'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['reputation.Reputation']"}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_Skills_skills_Skills)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['skill.Skill']"}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'personnegroupe_Tag_tag_Tag'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Telephone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'poigneemain.poignee': {
            'Meta': {'object_name': 'Poignee'},
            'Nombre': ('django.db.models.fields.FloatField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.categorie_code': {
            'Meta': {'object_name': 'Categorie_code'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.categorie_texte': {
            'Meta': {'object_name': 'Categorie_Texte'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Presentation_Categorie_Texte_NOte'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.categorie_texte_contenu': {
            'Meta': {'object_name': 'Categorie_Texte_contenu'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.code': {
            'Categorie': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Categorie_code']", 'null': 'True', 'blank': 'True'}),
            'Code': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte']", 'null': 'True', 'blank': 'True'}),
            'Couleur': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Couleur']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Code'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Code_Note_divers_notes_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.couleur': {
            'CodeHexa': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Couleur'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Couleur_Note_divers_notes_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.langue': {
            'Abreviation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Langue'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.miseenforme': {
            'Code': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'MiseEnForme'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'MiseEnForme_Note_divers_notes_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'StyleCss': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.StyleCss']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.stylecss': {
            'Code': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Code']", 'null': 'True', 'blank': 'True'}),
            'Couleur': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Couleur']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'StyleCss'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'StyleCss_Note_divers_notes_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.texte': {
            'Categorie': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Categorie_Texte']", 'null': 'True', 'blank': 'True'}),
            'Description': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Langue': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Langue']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Texte'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Presentation_Texte_NOte'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '4000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'presentation.texte_contenu': {
            'Categorie': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Categorie_Texte_contenu']", 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Texte_contenu'},
            'MiseEnForme': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.MiseEnForme']", 'null': 'True', 'blank': 'True'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Texte_contenu_Note_divers_notes_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'Texte': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['presentation.Texte']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'projet.date_visite': {
            'Date': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Date_Visite'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'projet.projet': {
            'Abo_Newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Article': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Article_Article_Article'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['article.Article']"}),
            'Date_Visite': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['projet.Date_Visite']", 'null': 'True', 'blank': 'True'}),
            'Date_creation': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Fiche': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fiche.Fiche']", 'null': 'True', 'blank': 'True'}),
            'Gallery': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['gallerie.Gallerie']", 'null': 'True', 'blank': 'True'}),
            'IP': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_IP_ip_IP'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['ip.IP']"}),
            'Importance': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Importance_importance_Importance'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['importance.Importance']"}),
            'Jugement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Jugement_jugement_Jugement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['jugement.Jugement']"}),
            'Kharma': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Kharma_kharma_Kharma'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['kharma.Kharma']"}),
            'Langue': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Langue_langue_Langue'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['langue.Langue']"}),
            'LienFacebook': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_LienFacebook_liens_LienFacebook'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienFacebook']"}),
            'LienTwitter': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_LienTwitter_liens_LienTwitter'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienTwitter']"}),
            'Liens': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Liens_liens_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Lieux_lieux_Lieux)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'Membre': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['membre.Membre']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'Projet'},
            'Naissance': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'Note_divers': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Note_divers_note_Note_divers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['note.Note_divers']"}),
            'PoigneeMain': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_PoigneeMain_poigneemain_PoigneeMain'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['poigneemain.Poignee']"}),
            'Referer': ('django.db.models.fields.CharField', [], {'max_length': '1500', 'null': 'True', 'blank': 'True'}),
            'Reputation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Reputation_reputation_Reputation'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['reputation.Reputation']"}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Skills_skills_Skills)'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['skill.Skill']"}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Tag_tag_Tag'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Tutorial': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Projet_Tutorial_tutorial_Tutorial'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tutorial.Tutorial']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'reputation.reputation': {
            'Meta': {'object_name': 'Reputation'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'skill.skill': {
            'FamilleTag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tag.FamilleTag']", 'symmetrical': 'False'}),
            'Meta': {'object_name': 'Skill'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tag.Tag']", 'symmetrical': 'False'}),
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '1500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tag.familletag': {
            'Meta': {'object_name': 'FamilleTag'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tag.Tag']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tag.tag': {
            'Creation': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Tag'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tutorial.categorietexte': {
            'Meta': {'object_name': 'CategorieTexte'},
            'Nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_categorietexte_visibilite'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tutorial.texte': {
            'CategorieTexte': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tutorial.CategorieTexte']", 'null': 'True', 'blank': 'True'}),
            'Date': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Texte_Date_date_Date'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['date.Date']"}),
            'Evenement': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Texte_Evenement_evenement_Evenement'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['evenement.Evenement']"}),
            'Image': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Texte_Image_image_image'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['image.Image']"}),
            'Info': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Texte_Info_info_Info'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['info.Info']"}),
            'Lien': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Texte_Lien_lien_Liens'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.Lien']"}),
            'LienFacebook': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Texte_LienFacebook_lien_LienTwitter'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lien.LienTwitter']"}),
            'Lieux': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Texte_Lieux_lieux_Lieux'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['lieux.Lieux']"}),
            'Meta': {'object_name': 'Texte'},
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Texte_Tag_tag_Tags'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Texte': ('django.db.models.fields.CharField', [], {'max_length': '100000'}),
            'Visibilite': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Texte_Visibilite_Visibilite_visibilite'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['visibilite.Visibilite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'tutorial.tutorial': {
            'Groupe': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Groupe_groupe_Groupe'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'GroupeCreateur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_GroupeCreateur_groupe_Groupe'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'GroupeReco': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_GroupeReco_groupe_Groupe'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['groupe.Groupe']"}),
            'MembreCreateur': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_MembreCreateur_membre_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'Meta': {'object_name': 'Tutorial'},
            'Notation': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Notation_notation_notation'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['notation.Notation']"}),
            'Skills': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Skills_skills_Skills'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['skill.Skill']"}),
            'Tag': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_Tag_tag_Tags'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['tag.Tag']"}),
            'Texte': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['tutorial.Texte']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membre': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_membre_membre_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"}),
            'membreReco': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Tutorial_membreReco_membre_Membre'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['membre.Membre']"})
        },
        'visibilite.visibilite': {
            'Meta': {'object_name': 'Visibilite'},
            'Visibilite': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['membre']
