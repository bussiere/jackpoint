# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
# Static analyzer import helpers: (STATIC_IMPORT_MARK)
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
    from gluon.validators import IS_UPPER #@UnusedImpor


import random

from gluon.storage import Storage



# def ensurefirstuser(firstname,lastname,email,password)​:
#     users = db(db.auth_user.email==email).​select()
#     if users:
#         user_id = users[0].id
#         created = False
#         if settings.debug_ensure_first_​user == True:
#             print ('found user_id so created equals %s') % created
#         return (user_id,created)

#     else:
#         my_crypt = CRYPT(key=auth.settings.hmac_​key)
#         crypt_pass = my_crypt(password)[0]        
#         id_user= db.auth_user.insert(
#                               ​     first_name=firstname,
#                               ​     last_name=lastname,
#                               ​     email = email,
#                               ​     password = crypt_pass
#                               ​     )
#         created = True
#         if settings.debug_ensure_first_​user == True:
#             print ('creating user_id')
#         return (id_user,created)

        


# def __ensure_users():
#     user_id, created = _ensure_user('first','last','e​mail@address.com','​UserPassword12345')
#     if settings.debug_ensure_users == True:
#         print ('user id %i') % user_id
#         print ('created %s') % created

# def __ensure_group_role(role,​description):
#     if not auth.id_group(role=role):    
#         auth.add_group(role=role,​description=description)    
#         if settings.debug_ensure_group_​role == True:
#             print ('created role %s') %(role)

# def __ensure_membership(group_id, user_id):
#     return_group_id = auth.add_membership(role=role, user_id=user_id)
#     if settings.debug_ensure_​membership == True:
#         print ('made user_id member of %s') %(role)
#     return return_group_id
 
# def __ensure_permissions(role, description, user_id):
#     __ensure_group_role(role,​description)
#     return_group_id = __ensure_membership(group_id, user_id)
#     if settings.debug_ensure_​permissions == True:
#         print return_group_id


def index():
    if auth.is_logged_in() :
        return "You get the blue pills"
    else :
        return dict(form=auth.login(),faq=URL('faq'))



def generate_invitation(number,word=4,num=1,numdigit=5):
    code = [
['BELCHER', 'FIX', 'EEL', 'PANZERBOY', 'DESK_JOCKEY', 'CHILLED', 'ENFORCER', 'CHERRY_PICKING', 'COUNTRY_CLUB', 'BOMBSHELL', 'PLUGGED_IN', 'FINI', 'LEGIT', 'JAM', 'BONED_OUT', 'BLADE', 'ROUST', 'SAMURAI', 'DISK', 'INPUT', 'POST_TIME', 'SOUNDS', 'SKIP', 'FLATBACKER', 'WILSON', 'SHOEMAKER', 'DELTA_SIERRA', 'HEART', 'CROAK', 'HEAD_HUNTER', 'HOSHO_KAISHA', "DELTA'D", "'FACE_(also,_FACE,_EYE-FACE,_I-FACE)", 'WEEFLE', 'DIRTGIRL', 'KEYBOARD', 'BRAIN_BUCKET', 'DRYING_OUT', 'OVERCOOK', 'PIG', 'COLD_TEA', 'RECONFIG', 'PAD', 'LIT_UP', 'WRAITH', 'HANDLE', 'L.P.', 'PINCH', 'TAKE_A_CAB', 'SPILL', 'ACE_KOOL', 'DO', 'BIZ', 'BROWNIE', 'CANDLE_AND_BLOOD', 'BLUEBOY', 'UP_ON_IT', 'BURN', 'USER_INTERFACE', 'HOB', 'GYRO', 'STUFFIT', 'THATCH', 'ICEBREAKER', 'ZIP_GUN', 'PETERMAN', 'PLAY_DOUGH', 'TREY-EIGHT', 'SETTLE', "CHIPPIN'_IN", 'MEATBALL', 'RAFFLES', 'YUBITSUME', 'CROAKER', 'SUCKER_POCKETS', 'L.A.M.A.', 'GEEK', 'BUTTONHEAD'],
['TAKE', 'TEKIYA', 'KURUMAKU', 'BLOC', 'GAT', 'JOHATSU', 'CRYSTAL', 'A.I.', 'ZEROED', 'OVER_THE_SHOULDER', 'GRAB_GEE', 'PANZER', 'GO_LEO', 'WASHED', 'I.C.E.', 'COPSHOP', 'COLLATERAL_DAMAGE', 'BIG_DARK', 'DOUBLE-DEUCE', 'ZONEDANCE', 'MARK', 'COBBERS', 'CHIMPIRA', 'TRIADS', 'SHANK', 'FRAG', 'BREATH_VAC', "CHARLIE'S_ANGEL", 'MULE', 'BURNER', "PACKIN'", 'HOTDOGGER', 'BOSOZOKU', 'RIPPERDOC', 'THIRDMAN', 'MAXIMUM,_MAX', 'CHOOH2_("CHOO")', 'CRYO_MAX', 'HEATER', 'SHARK', 'JOYGIRL', 'GURENTAI', 'BANDIT', 'VENICE', 'MIZU_SHOBAI', 'PASTA_BOYS', 'SQUID', 'CYBERED_UP', 'DEAD_RECKONING', 'POPSICLE', 'FAUST', 'COLLARBOY', 'SHOES', 'TORCH', 'DELTAJOCK', 'BUTTERFLY_MAN', 'WISE_GUYS', 'BOOST', 'CAIN', 'FOUR-FIVE', 'BREAK-DOWN', 'POLYMER_ONE-SHOT', 'FLAG', 'CALL_GIRL', 'IN_THE_HUNT', 'HYDRO', 'DOCK', 'FENCE', 'SHAIKUJIN', 'GOMI', 'FILTER', 'SAINT_NICK', 'LINEFOOT', 'CAVALRY', 'PUKE', 'CONVERSION', 'FINGER', 'CONTRACT'],
['PLASTIC', 'CRYSTALJOCKEY,_CRYSTALJOCK', 'SCREW', 'TOYSTORE', 'DREAM_TIME', 'EXOTIC', 'WALKABOUT', 'DIAMOND_SEASON', 'SARAKIN', 'CHRISTMAS_BUNDLES', 'SHADES', 'BUTTON_MAN', 'FOXTROT_UNIFORM', 'KAI', 'UNDER_THE_PAINT', 'MINIMUM', 'TRIPLE_A', 'PIG_ON_A_WHEEL', 'BAG_MAN', 'DIP', 'PIGEONS', 'MAN', 'ADAM_HENRY', 'HIGH', 'HEAT', 'NINJO', 'KNIFE_FIGHT', 'MOUTHPIECE', 'AGRIPLEX', 'DATA_TERM', 'LIZ', 'CHROMER', 'OUTPUT', 'N.O.E.', 'CLOSE_A_CONTRACT', 'LASSIE', 'FLATLINE', 'CHIV', 'SING', 'AMMO', 'RAT', 'MATCHBOX', 'PULL_AN_ASH', 'BORYOKUDAN', 'SQUEEZE', 'RONIN', 'HIT', 'RAGS', 'TAKE_OUT', 'BEAT_THE_RAP', 'GIRI', 'RUNNING_THE_LINE', 'HARNESS', 'GRAVEROBBER', 'DROP_A_DIME', 'BADGE_ON_A_BEAVER', 'FLETCHER', 'AMPED-OUT', 'NEUTRALIZE', 'PETER', 'CONFIG', 'HARDFIRE', 'B.A.M.A.', 'CHROMATIC_ROCK', 'MOLDED', 'RAD', 'CREASED', 'CHATTER_BOX', 'HAND_CANNON', 'NIPPERS', 'SIERRA_HOTEL', 'HOOK_UP', '-JOCKEY,_-JOCK', 'BUG', 'BATMAN_AND_ROBIN', 'BLACK_OPERATIONS', "D.C.'S", 'SO_KA'],
['_A.A.A.', 'HOME_PLATE', 'LITEJACK', 'PINEAPPLE', 'MAKE', 'THE_STREET', 'SITREP', 'HANGING_PAPER', 'PAINT_BOYS', 'WETWORK', 'NINER', 'BOOKIE', 'WHIPLASH', 'TORPEDO', 'HEATWAVE', 'SOLAR_WIND', 'QUIFF', 'BIKE', 'TRAFFIC', 'WIRE_ROOM', 'OYABUN', 'COWBOY', 'KOBUN', 'MUDBOY', 'COP_OUT', 'SOKAIYA', "'DORPH", 'JOYBOY', 'DIRTY', 'BOAT', 'DROP', 'GRAV_or_GEE', 'APOGEE', 'BOOSTER', 'BOOK', 'FRY', 'PULLING_TEETH', 'ONE_LARGE', 'COMBAT_DRUGS', 'THRASH', 'DO_A_GHOST', 'DELTA', 'RIN_TIN_TIN', 'DROP_OUT', 'GUMI', 'ROCKERBOY/GIRL', 'BULLET', 'DEB', 'THREADING_THE_NEEDLE', 'MOTOR', 'BLEEDER', 'ARC', 'BOPPER', 'WASTE', '_______DEMUKAI', 'BREAK', 'HOLDING_DOWN', 'FEDS', 'GAP', 'RABBI', 'BAKUTO', 'CHOMBATTA_(CHOOMBA)', 'BIG_HATS', 'MR._JOHNSON', 'EXEC', 'BULL', 'BULLSEYE', 'POSERGANG', 'CHAOL', 'GEISHA', 'SLAMMIT_ON', 'POP_CAPS', 'HARD_TIME', 'BENJI', 'MAKING_BANK', 'PAPERHANGER', 'NETRUN', 'BOGEY'],
]     
    i = 0
    invits = []
    print number
    while (i < number):
        invit = ""
        j = 0
        while (j < word):
            debut = random.randint(0,len(code)-1)
            codepick = code[debut][random.randint(0,len(code[debut])-1)]
            j += 1
            invit += codepick+"-"
        j = 0
        while (j < num):
            invit += randomdig(numdigit)+"-"
            j += 1
        i+= 1
        invit = invit[:-1]
        if invit not in invits :
            invits.append(invit[:-1])
            print invit
    return invits
        
def randomdig(number):
    max = "9"*number
    max = int(max)
    rand =  random.randint(0,max)
    rand = str(rand)
    rand = "0"*(number-len(rand))+rand
    return rand

@auth.requires_login()
def inscription():
    form = SQLFORM(db[auth.settings.table_user_name])
    return dict(form=form)

def liste_invitations():
    return dict(rows = db().select(db.Invitation.ALL))

#@auth.requires_membership('manager')
def generate_invitationpage():
   form=FORM("Nombre d'invit a générer:", INPUT(_name='nmbreinvit'), INPUT(_type='submit'))
   if form.process().accepted:
       i = form.vars.nmbreinvit
       invitsgenere = generate_invitation(int(i))
       for invit in invitsgenere :
           db.Invitation.insert(Code=invit)
           db.commit()
       session.flash = 'invitation inserted'
       form=FORM("Nombre d'invit a générer:", INPUT(_name='nmbreinvit'), INPUT(_type='submit'))
       #db.Invitation.insert(Code="Toto-5542")
       db.commit()
   return dict(form=form)

def verif_invitation(form):
    if len(db(db.Invitation.Code==form.vars.invitation).select()) != 1 :
        form.errors('code invitation incorrect')


def invitation():
    form=FORM("Code Invitation :", INPUT(_name='invitation'),INPUT(_name='email'),  INPUT(_type='submit'))
    if form.process(onvalidation=verif_invitation) :
        user = "" #__ensure_first_user("john","doe",form.vars.email,form.vars.invitation)​
        auth.user = Storage(auth.settings.table_user._filter_fields(user, id=True))
        auth.environment.session.auth = Storage(user=user, last_visit=request.now,
                                            expiration=auth.settings.expiration)
        redirect(URL('inscription'))
    return dict(form=form)

def faq():

    return dict()
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
