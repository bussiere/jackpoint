# -*- coding: utf-8 -*-
# Static analyzer import helpers:
if 0: 
    import gluon
    global cache; cache = gluon.cache.Cache()
    global LOAD; LOAD  = gluon.compileapp.LoadFactory()
    import gluon.compileapp.local_import_aux as local_import #@UnusedImport
    from gluon.contrib.gql import GQLDB #@UnusedImport
    from gluon.dal import Field #@UnusedImport
    global request; request = gluon.globals.Request()
    global response; response = gluon.globals.Response()
    global session; session = gluon.globals.Session()
    from gluon.html import A #@UnusedImport
    from gluon.html import B #@UnusedImport
    from gluon.html import BEAUTIFY #@UnusedImport
    from gluon.html import BODY #@UnusedImport
    from gluon.html import BR #@UnusedImport
    from gluon.html import CENTER #@UnusedImport
    from gluon.html import CODE #@UnusedImport
    from gluon.html import DIV #@UnusedImport
    from gluon.html import EM #@UnusedImport
    from gluon.html import EMBED #@UnusedImport
    from gluon.html import embed64 #@UnusedImport
    from gluon.html import FIELDSET #@UnusedImport
    from gluon.html import FORM #@UnusedImport
    from gluon.html import H1 #@UnusedImport
    from gluon.html import H2 #@UnusedImport
    from gluon.html import H3 #@UnusedImport
    from gluon.html import H4 #@UnusedImport
    from gluon.html import H5 #@UnusedImport
    from gluon.html import H6 #@UnusedImport
    from gluon.html import HEAD #@UnusedImport
    from gluon.html import HR #@UnusedImport
    from gluon.html import HTML #@UnusedImport
    from gluon.html import I #@UnusedImport
    from gluon.html import IFRAME #@UnusedImport
    from gluon.html import IMG #@UnusedImport
    from gluon.html import INPUT #@UnusedImport
    from gluon.html import LABEL #@UnusedImport
    from gluon.html import LEGEND #@UnusedImport
    from gluon.html import LI #@UnusedImport
    from gluon.html import LINK #@UnusedImport
    from gluon.html import MARKMIN #@UnusedImport
    from gluon.html import MENU #@UnusedImport
    from gluon.html import META #@UnusedImport
    from gluon.html import OBJECT #@UnusedImport
    from gluon.html import OL #@UnusedImport
    from gluon.html import ON #@UnusedImport
    from gluon.html import OPTGROUP #@UnusedImport
    from gluon.html import OPTION #@UnusedImport
    from gluon.html import P #@UnusedImport
    from gluon.html import PRE #@UnusedImport
    from gluon.html import STYLE #@UnusedImport
    from gluon.html import SCRIPT #@UnusedImport
    from gluon.html import SELECT #@UnusedImport
    from gluon.html import SPAN #@UnusedImport
    from gluon.html import TABLE #@UnusedImport
    from gluon.html import TAG #@UnusedImport
    from gluon.html import TBODY #@UnusedImport
    from gluon.html import TD #@UnusedImport
    from gluon.html import TEXTAREA #@UnusedImport
    from gluon.html import TFOOT #@UnusedImport
    from gluon.html import TH  #@UnusedImport
    from gluon.html import THEAD #@UnusedImport
    from gluon.html import TITLE #@UnusedImport
    from gluon.html import TR #@UnusedImport
    from gluon.html import TT #@UnusedImport
    from gluon.html import UL #@UnusedImport
    from gluon.html import URL #@UnusedImport
    from gluon.html import XHTML #@UnusedImport
    from gluon.html import XML #@UnusedImport
    from gluon.html import xmlescape #@UnusedImport
    from gluon.http import HTTP #@UnusedImport
    from gluon.http import redirect #@UnusedImport
    import gluon.languages.translator as T #@UnusedImport
    from gluon.sql import DAL
    global db; db = DAL()
    from gluon.sql import SQLDB #@UnusedImport
    from gluon.sql import SQLField #@UnusedImport
    from gluon.sqlhtml import SQLFORM #@UnusedImport
    from gluon.sqlhtml import SQLTABLE #@UnusedImport
    from gluon.tools import  Auth
    global auth; auth = Auth()
    from gluon.tools import Crud
    global crud; crud = Crud()
    from gluon.tools import fetch #@UnusedImport
    from gluon.tools import geocode #@UnusedImport
    from gluon.tools import Mail
    global mail; mail = Mail()
    from gluon.tools import PluginManager
    global plugins; plugins = PluginManager()
    from gluon.tools import prettydate #@UnusedImport
    from gluon.tools import Recaptcha #@UnusedImport
    from gluon.tools import Service
    global service; service = Service()
    from gluon.validators import CLEANUP  #@UnusedImport
    from gluon.validators import CRYPT #@UnusedImport
    from gluon.validators import IS_ALPHANUMERIC #@UnusedImport
    from gluon.validators import IS_DATE #@UnusedImport
    from gluon.validators import IS_DATE_IN_RANGE #@UnusedImport
    from gluon.validators import IS_DATETIME #@UnusedImport
    from gluon.validators import IS_DATETIME_IN_RANGE #@UnusedImport
    from gluon.validators import IS_DECIMAL_IN_RANGE #@UnusedImport
    from gluon.validators import IS_EMAIL #@UnusedImport
    from gluon.validators import IS_EMPTY_OR #@UnusedImport
    from gluon.validators import IS_EQUAL_TO #@UnusedImport
    from gluon.validators import IS_EXPR #@UnusedImport
    from gluon.validators import IS_FLOAT_IN_RANGE #@UnusedImport
    from gluon.validators import IS_IMAGE #@UnusedImport
    from gluon.validators import IS_IN_DB #@UnusedImport
    from gluon.validators import IS_IN_SET #@UnusedImport
    from gluon.validators import IS_INT_IN_RANGE #@UnusedImport
    from gluon.validators import IS_IPV4 #@UnusedImport
    from gluon.validators import IS_LENGTH #@UnusedImport
    from gluon.validators import IS_LIST_OF #@UnusedImport
    from gluon.validators import IS_LOWER #@UnusedImport
    from gluon.validators import IS_MATCH #@UnusedImport
    from gluon.validators import IS_NOT_EMPTY #@UnusedImport
    from gluon.validators import IS_NOT_IN_DB #@UnusedImport
    from gluon.validators import IS_NULL_OR #@UnusedImport
    from gluon.validators import IS_SLUG #@UnusedImport
    from gluon.validators import IS_STRONG  #@UnusedImport
    from gluon.validators import IS_TIME #@UnusedImport
    from gluon.validators import IS_UPLOAD_FILENAME #@UnusedImport
    from gluon.validators import IS_UPPER #@UnusedImport
    from gluon.validators import IS_URL #@UnusedImport
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
#from gluon.contrib.memdb import MEMDB
#from google.appengine.api.memcache import Client
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


db.define_table('Skill',
 Field('Nom', unique=True),
 format = '%(Nom)s')

db.define_table('SkillLevel',
 Field('Level', 'integer'),
 Field('Skill', db.Skill),
 Field('Parent', db.Skill),
 format = '%(Skill)s')



db.define_table('SkillLevelUser',
 Field('Skill', db.SkillLevel),
 Field('Niveau','integer'),
 Field('Private','boolean'),
 format = '%(Skill)s')


db.define_table('Carac',
 Field('Nom', unique=True),
 format = '%(Nom)s')


db.define_table('CaracUse',
 Field('Carac', db.Skill),
 Field('Niveau','integer'),
 Field('Private','boolean'),
 format = '%(Skill)s')



db.define_table('Item',
 Field('Nom', unique=True),
 Field('Skill', db.Skill),
 format = '%(Nom)s')




db.define_table(
auth.settings.table_user_name,
Field('username', length=128, default=''),
Field('invitation'),
Field('email', length=128, default='', unique=True), # required
Field('password', 'password', length=512,# required
readable=False, label='Password'),
Field('Skills','list:reference SkillLevelUser',default=None),
Field('validated','boolean',default=False),
Field('Items','list:reference Item',default=None),
Field('registration_key', length=512,# required
writable=False, readable=False, default=''),
Field('reset_password_key', length=512,# required
writable=False, readable=False, default=''),
Field('registration_id', length=512, # required
writable=False, readable=False, default=''))

## do not forget validators
custom_auth_table = db[auth.settings.table_user_name] # get the custom_auth_table
custom_auth_table.username.requires = \
IS_NOT_EMPTY(error_message=auth.messages.is_empty)
custom_auth_table.password.requires = [CRYPT()]
custom_auth_table.email.requires = [
IS_EMAIL(error_message=auth.messages.invalid_email),
IS_NOT_IN_DB(db, custom_auth_table.email)]


## create all tables needed by auth if not custom tables
auth.define_tables()

db.define_table('Father',
Field('father', db.auth_user),
Field('sons', 'list:reference auth_user'),
format = '%(Nom)s')

db.define_table('Son',
Field('father', db.auth_user),
Field('sons', db.auth_user),
format = '%(Nom)s')



db.define_table('Suggestion',
 Field('User',db.auth_user),
 Field('Texte'),
 Field('Done','boolean',default=False),
 format = '%(Skill)s')




 
db.SkillLevelUser.Niveau.requires=IS_INT_IN_RANGE(0, 5)

db.define_table('SkillDemande',
 Field('Skill', db.Skill),
 Field('Niveau','integer'),
 format = '%(Niveau)s') 


db.SkillDemande.Niveau.requires=IS_INT_IN_RANGE(0, 5)
 
 


db.define_table('Demande',
 Field('Topic', unique=True),
 Field('Texte'),
 Field('Skills','list:reference SkillDemande'),
 Field('Items','list:reference Item'),
 Field('auth_user',db.auth_user),
 format = '%(Topic)s')

db.define_table('Usage_Db',
 Field('Nom', unique=True),
 format = '%(Nom)s')

db.define_table('Invitation',
 Field('Code', unique=True),
 Field('Usage', db.Usage_Db),
 Field('Donneur', db.auth_user),
 Field('Receveur', db.auth_user),
 Field('Email'),
 Field('Used', 'boolean'),
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
 
db.define_table('Tip',
 Field('Texte'),
 Field('User',db.auth_user),
 Field('Validation','boolean'),
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
## 'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

