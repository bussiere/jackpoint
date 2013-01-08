import random

def generate_invitation(number,word=4,num=1,numdigit=5):
    code = [
['BELCHER', 'FIX', 'EEL', 'PANZERBOY', 'DESK_JOCKEY', 'CHILLED', 'ENFORCER', 'CHERRY_PICKING', 'COUNTRY_CLUB', 'BOMBSHELL', 'PLUGGED_IN', 'FINI', 'LEGIT', 'JAM', 'BONED_OUT', 'BLADE', 'ROUST', 'SAMURAI', 'DISK', 'INPUT', 'POST_TIME', 'SOUNDS', 'SKIP', 'FLATBACKER', 'WILSON', 'SHOEMAKER', 'DELTA_SIERRA', 'HEART', 'CROAK', 'HEAD_HUNTER', 'HOSHO_KAISHA', "DELTA'D", "FACE_FACE_EYE_FACE_I_FACE", 'WEEFLE', 'DIRTGIRL', 'KEYBOARD', 'BRAIN_BUCKET', 'DRYING_OUT', 'OVERCOOK', 'PIG', 'COLD_TEA', 'RECONFIG', 'PAD', 'LIT_UP', 'WRAITH', 'HANDLE', 'L.P.', 'PINCH', 'TAKE_A_CAB', 'SPILL', 'ACE_KOOL', 'DO', 'BIZ', 'BROWNIE', 'CANDLE_AND_BLOOD', 'BLUEBOY', 'UP_ON_IT', 'BURN', 'USER_INTERFACE', 'HOB', 'GYRO', 'STUFFIT', 'THATCH', 'ICEBREAKER', 'ZIP_GUN', 'PETERMAN', 'PLAY_DOUGH', 'TREY-EIGHT', 'SETTLE', "CHIPPIN'_IN", 'MEATBALL', 'RAFFLES', 'YUBITSUME', 'CROAKER', 'SUCKER_POCKETS', 'L.A.M.A.', 'GEEK', 'BUTTONHEAD'],
['TAKE', 'TEKIYA', 'KURUMAKU', 'BLOC', 'GAT', 'JOHATSU', 'CRYSTAL', 'A.I.', 'ZEROED', 'OVER_THE_SHOULDER', 'GRAB_GEE', 'PANZER', 'GO_LEO', 'WASHED', 'I.C.E.', 'COPSHOP', 'COLLATERAL_DAMAGE', 'BIG_DARK', 'DOUBLE-DEUCE', 'ZONEDANCE', 'MARK', 'COBBERS', 'CHIMPIRA', 'TRIADS', 'SHANK', 'FRAG', 'BREATH_VAC', "CHARLIE'S_ANGEL", 'MULE', 'BURNER', "PACKIN", 'HOTDOGGER', 'BOSOZOKU', 'RIPPERDOC', 'THIRDMAN', 'MAXIMUM,_MAX', 'CHOOH2_CHOO', 'CRYO_MAX', 'HEATER', 'SHARK', 'JOYGIRL', 'GURENTAI', 'BANDIT', 'VENICE', 'MIZU_SHOBAI', 'PASTA_BOYS', 'SQUID', 'CYBERED_UP', 'DEAD_RECKONING', 'POPSICLE', 'FAUST', 'COLLARBOY', 'SHOES', 'TORCH', 'DELTAJOCK', 'BUTTERFLY_MAN', 'WISE_GUYS', 'BOOST', 'CAIN', 'FOUR-FIVE', 'BREAK-DOWN', 'POLYMER_ONE-SHOT', 'FLAG', 'CALL_GIRL', 'IN_THE_HUNT', 'HYDRO', 'DOCK', 'FENCE', 'SHAIKUJIN', 'GOMI', 'FILTER', 'SAINT_NICK', 'LINEFOOT', 'CAVALRY', 'PUKE', 'CONVERSION', 'FINGER', 'CONTRACT'],
['PLASTIC', 'CRYSTALJOCKEY,_CRYSTALJOCK', 'SCREW', 'TOYSTORE', 'DREAM_TIME', 'EXOTIC', 'WALKABOUT', 'DIAMOND_SEASON', 'SARAKIN', 'CHRISTMAS_BUNDLES', 'SHADES', 'BUTTON_MAN', 'FOXTROT_UNIFORM', 'KAI', 'UNDER_THE_PAINT', 'MINIMUM', 'TRIPLE_A', 'PIG_ON_A_WHEEL', 'BAG_MAN', 'DIP', 'PIGEONS', 'MAN', 'ADAM_HENRY', 'HIGH', 'HEAT', 'NINJO', 'KNIFE_FIGHT', 'MOUTHPIECE', 'AGRIPLEX', 'DATA_TERM', 'LIZ', 'CHROMER', 'OUTPUT', 'N.O.E.', 'CLOSE_A_CONTRACT', 'LASSIE', 'FLATLINE', 'CHIV', 'SING', 'AMMO', 'RAT', 'MATCHBOX', 'PULL_AN_ASH', 'BORYOKUDAN', 'SQUEEZE', 'RONIN', 'HIT', 'RAGS', 'TAKE_OUT', 'BEAT_THE_RAP', 'GIRI', 'RUNNING_THE_LINE', 'HARNESS', 'GRAVEROBBER', 'DROP_A_DIME', 'BADGE_ON_A_BEAVER', 'FLETCHER', 'AMPED-OUT', 'NEUTRALIZE', 'PETER', 'CONFIG', 'HARDFIRE', 'B.A.M.A.', 'CHROMATIC_ROCK', 'MOLDED', 'RAD', 'CREASED', 'CHATTER_BOX', 'HAND_CANNON', 'NIPPERS', 'SIERRA_HOTEL', 'HOOK_UP', 'JOCKEYJOCK', 'BUG', 'BATMAN_AND_ROBIN', 'BLACK_OPERATIONS', "D.C.S", 'SO_KA'],
['A.A.A.', 'HOME_PLATE', 'LITEJACK', 'PINEAPPLE', 'MAKE', 'THE_STREET', 'SITREP', 'HANGING_PAPER', 'PAINT_BOYS', 'WETWORK', 'NINER', 'BOOKIE', 'WHIPLASH', 'TORPEDO', 'HEATWAVE', 'SOLAR_WIND', 'QUIFF', 'BIKE', 'TRAFFIC', 'WIRE_ROOM', 'OYABUN', 'COWBOY', 'KOBUN', 'MUDBOY', 'COP_OUT', 'SOKAIYA', "'DORPH", 'JOYBOY', 'DIRTY', 'BOAT', 'DROP', 'GRAV_or_GEE', 'APOGEE', 'BOOSTER', 'BOOK', 'FRY', 'PULLING_TEETH', 'ONE_LARGE', 'COMBAT_DRUGS', 'THRASH', 'DO_A_GHOST', 'DELTA', 'RIN_TIN_TIN', 'DROP_OUT', 'GUMI', 'ROCKERBOY_GIRL', 'BULLET', 'DEB', 'ThreadEngineING_THE_NEEDLE', 'MOTOR', 'BLEEDER', 'ARC', 'BOPPER', 'WASTE', '_______DEMUKAI', 'BREAK', 'HOLDING_DOWN', 'FEDS', 'GAP', 'RABBI', 'BAKUTO', 'CHOMBATTA_CHOOMBA', 'BIG_HATS', 'MR._JOHNSON', 'EXEC', 'BULL', 'BULLSEYE', 'POSERGANG', 'CHAOL', 'GEISHA', 'SLAMMIT_ON', 'POP_CAPS', 'HARD_TIME', 'BENJI', 'MAKING_BANK', 'PAPERHANGER', 'NETRUN', 'BOGEY'],
]     
    i = 0
    invits = []
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
    return invits
        
def randomdig(number):
    max = "9"*number
    max = int(max)
    rand =  random.randint(0,max)
    rand = str(rand)
    rand = "0"*(number-len(rand))+rand
    return rand


def classer_invitation(invitation,user=None):
    from invitation.models import Invitation,InvitationUsed
    # ca merde ici
    invitationget = Invitation.objects.get(Code=invitation)
    invitationget.Used = True
    invitationget.save()
    if user != None :
        invitationused = InvitationUsed.objects.create(Code=invitation) 
        invitationused.Donneur = user
        invitationused.save()
    else :
        invitationused = InvitationUsed.objects.create(Code=invitation) 
        invitationused.save()
        
    
    


if __name__ == '__main__':
    print randomdig(5)
    print generate_invitation(5,4,1,5)
    print generate_invitation(5)