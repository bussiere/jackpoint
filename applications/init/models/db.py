# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite')
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db = db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key())
crud, service, plugins = Crud(db), Service(), PluginManager()
db.define_table(
    auth.settings.table_user_name,
    Field('first_name', length=128, default=''),
    Field('last_name', length=128, default=''),
    Field('email', length=128, default='', unique=True), # required
    Field('password', 'password', length=512,            # required
          readable=False, label='Password'),
    Field('Skills','list:reference SkillUser'),
    Field('Items','list:reference Item'),
    Field('registration_key', length=512,                # required
          writable=False, readable=False, default=''),
    Field('reset_password_key', length=512,              # required
          writable=False, readable=False, default=''),
    Field('registration_id', length=512,                 # required
          writable=False, readable=False, default=''))

## do not forget validators
custom_auth_table = db[auth.settings.table_user_name] # get the custom_auth_table
custom_auth_table.first_name.requires = \
  IS_NOT_EMPTY(error_message=auth.messages.is_empty)
custom_auth_table.last_name.requires = \
  IS_NOT_EMPTY(error_message=auth.messages.is_empty)
custom_auth_table.password.requires = [CRYPT()]
custom_auth_table.email.requires = [
  IS_EMAIL(error_message=auth.messages.invalid_email),
  IS_NOT_IN_DB(db, custom_auth_table.email)]

  
## create all tables needed by auth if not custom tables
auth.define_tables()

db.define_table('Skill',
   Field('Nom', unique=True),
   format = '%(Nom)s')

db.define_table('Item',
   Field('Nom', unique=True),
   format = '%(Nom)s')


db.define_table('SkillUser',
   Field('Skill', db.Skill),
   Field('User', db.auth_user),
   Field('Niveau','integer'),
   format = '%(Demande)s')
   
db.SkillUser.Niveau.requires=IS_INT_IN_RANGE(0, 5)

db.define_table('SkillDemande',
   Field('Skill', db.Skill),
   Field('Niveau','integer'),
   format = '%(Demande)s') 


db.SkillDemande.Niveau.requires=IS_INT_IN_RANGE(0, 5)
   
   


db.define_table('Demande',
   Field('Topic', unique=True),
   Field('Texte'),
   Field('Skills','list:reference SkillDemande'),
   Field('Items','list:reference Item'),
   Field('auth_user',db.auth_user),
   format = '%(Topic)s')

db.define_table('Invitation',
   Field('Code', unique=True),
   format = '%(Topic)s')

db.define_table('Popup',
   Field('Demande', db.Demande),
   Field('User', db.auth_user),
   format = '%(Demande)s')

db.define_table('Suggestion',
   Field('Topic', unique=True),
   Field('Texte'),
   Field('Skills','list:reference Skill'),
   Field('Items','list:reference Item'),
   Field('auth_user',db.auth_user),
   format = '%(Topic)s')
   


## configure email
mail=auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth,filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

