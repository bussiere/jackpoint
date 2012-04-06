import random
text = """
 A.A.A. - Anti-aircraft artillery.

        ACE KOOL - (gang) Best friend.  Back-up.

        ADAM HENRY - (cop) Pheonetic alphabet for "Ass Hole".

        AGRIPLEX - An agglomeration of farms with one central managment
        complex.  A modern day capitalist collective farm.

        A.I. - Artificial Intelligence; a computer with full self awareness.

        AMMO - Ammunition.

        AMPED-OUT - Fatigue after being under the influence of amphetamines
        and certain combat drugs.

        APOGEE - The best.  The greatest.

        ARC - An arcology.

        BADGE ON A BEAVER - A female officer.

        BAG MAN - A fixer or fence.

        BAKUTO - (jap) Gambler.

        B.A.M.A. - Boston-Atlantic Metropolitan Access.

        BANDIT - An enemy aircraft.

        BATMAN AND ROBIN - Two officers in a patrol car.

        BEAT THE RAP - To get acquitted.

        BELCHER - An informer.

        BENJI - A robohound.

        BIG DARK - Space.

        BIG HATS - State police.

        BIKE - A motorcycle.

        BIZ - Crime.

        BLACK OPERATIONS - Illegal or secret missions.

        BLADE - A knife.

        BLEEDER - An extortionist.

        BLOC - A cartel composed of Orbital concerns with similar capa-
        bilities and interests, i.e., the Aerospace Bloc, the Pharmaceutical
        Bloc, etc.

        BLUEBOY - Local or state police.

        BOAT - A submarine, no matter how large.

        BOGEY - An unidentified aircraft.

        BOMBSHELL - 1. Evacuate quickly.  2. Run.

        BONED OUT - Quit, chickened-out, left.

        BOOK - 1. To run away, get out, or leave.  2. A bookmaker's betting
        organization.

        BOOKIE - One who takes bets and "makes book".

        BOOST - To shoplift or steal.

        BOOSTER - Any member of a gang that effects cyberware, leather
        clothing, and random violence.

        BOPPER - A hit man.

        BORYOKUDAN - (jap) Literally, violence groups.  Used by Japanese
        police to refer to Yakuza.

        BOSOZOKU - (jap) Motorcycle and hot-rod gangs, a prime source
        of Yakuza recruits.

        BRAIN BUCKET - A motorcycle helmet.

        BREAK - To run or get away.

        BREAK-DOWN - A shotgun.

        BREATH VAC - To run out of air.

        BROWNIE - A traffic cop.

        BUG - A listening device or wire.

        BULL - 1. A prison guard.  2. A police officer.

        BULLET - One year in custody.

        BULLSEYE - A light tatoo on any exposed skin.

        BURN - 1. To shoot, esp with a laser.  2. To electrocute.

        BURNER - A laser beam splitter.

        BUTTERFLY MAN - A forger.

        BUTTONHEAD - A person addicted to stimulating the pleasure centers
        through interface sockets.

        BUTTON MAN - Someone who selects or points out the job.

        CAIN - A traitor, a backstabber.

        CALL GIRL - A high-priced prostitute.

        CANDLE AND BLOOD - Initiation into the mafia.

        CAVALRY - Police reinforcements.

        CHAOL - To be tough; a real stud.

        CHARLIE'S ANGEL - A female officer.

        CHATTER BOX - A machine gun.

        CHERRY PICKING - (Motorcyclist) When an expert rider enters
        a lower-division race to score an easy win.

        CHILLED - To be cool; to be together.

        CHIMPIRA - (jap) Derived from the Japanese word for "penis";
        it is used on the street as Americans might use the word
        "prick".

        CHIPPIN' IN - 1. To buy cyberware for the first time.  2. To cast
        your lot with a group.  3. To connect with a machine.

        CHIV - Knife.

        CHOMBATTA (CHOOMBA) - Neo-Afro-American slang for a friend or a
        family member.

        CHOOH2 ("CHOO") - Streetslang for alcohol, as used in vehicle power
        plants.

        CHRISTMAS BUNDLES - Large sums of money.

        CHROMER - 21st century heavy metal rock fan.

        CHROMATIC ROCK - A type of heavy metal characterized by heavy
        electronics, simple rythms, and violent lyrics.

        CLOSE A CONTRACT - To kill.

        COBBERS - Your buddies or members of your work gang.

        COLD TEA - Alcohol.

        COLLARBOY - (derogatory) 1. A white collar worker.  2. An Orbital
        employee.  3. An Orbital fellow-traveller.

        COLLATERAL DAMAGE - Civillian casualties.

        COMBAT DRUGS - Any one of a series of designer drugs created to
        increase speed, stamina, and reflexes.

        CONFIG - To arrange something, as in, "I configged to dock with
        her."

        CONTRACT - Hired to kill.

        CONVERSION - A full cyborg conversion.

        COP OUT - To quit.

        COPSHOP - Police station.

        COUNTRY CLUB - A minimum security facility.

        COWBOY - A Netrunner.

        CREASED - Killed.

        CROAK - To kill.

        CROAKER - A doctor.

        CRYO MAX - A contemporary fashion based on 19th century Russian
        Romantic dress (cossack boots, colorful sashes, brocaded dol-
        mans, etc) mixed with high-tech accreations, such as cybertech.

        CRYSTAL - 1. A liquid crystal computer matrix.  2. Anything, such
        as an artificial intelligence, cybertech, or even software, using
        or operated by an LC matrix.

        CRYSTALJOCKEY, CRYSTALJOCK - A computer user, a netrunner.

        CYBERED UP - To get as much cyberware implanted as possible before
        you go over the Edge.

        DATA TERM - A streetcorner information machine with a screen,
        'Net inputs, and keyboard.

        D.C.'S - Federal officers.

        DEAD RECKONING - Navigating without instruments.

        DEB - A pre-operation transexual.

        DELTA - (U.S. Slang) A smuggling aircraft.

        DELTA'D - To make maximum speed towards a place.

        DELTAJOCK - A Delta pilot; and air smuggler.

        DELTA SIERRA - Dog Shit.

       DEMUKAI - (jap) The Yakuza prison-release ceremony

        DERM - A slap patch used to administer contact drugs.

        DESK JOCKEY - A white collar guy.

        DIAMOND SEASON - Warm weather.

        DIP - A pickpocket.

        DIRTGIRL - (derogatory Orbital slang) An Earth woman.

        DIRTY - To possess drugs or be under the influence.

        DISK - Record, recording, or a laser disk.

        DO - To kill.

        DO A GHOST - To leave the scene of a crime.

        DOCK - 1. To meet someone.  2. To have sex.

        'DORPH - Streetslang for synthetic endorphins, a designer drug
        that increases healing powers, limits fatigue, and produces a
        "rush" similar to a second wind.

        DOUBLE-DEUCE - A .22 caliber gun.

        DREAM TIME - Jail time in braindance.

        DROP - 1. Receiver of stolen goods.  2. To kill.

        DROP A DIME - To snitch on someone.

        DROP OUT - Go back to Earth or Luna.

        DRYING OUT - Abstaining from alcohol.

        EEL - An escape artist.

        ENFORCER - Someone who carries out or enforces instructions of a
        criminal boss, usually through physical intimidation.

        EXEC - A corporate executive.

        EXOTIC - A human biosculpted with non-human elements; fur,
        long ears, fangs, etc.

        'FACE (also, FACE, EYE-FACE, I-FACE) - The Interface.
        Jacking into the 'Net.

        FAUST - A netrunner who deals in, or with, A.I.'s.

        FEDS - Federal officers.

        FENCE - Someone who buys and sells stolen goods.

        FILTER - A gas mask.

        FINGER - To point out or identify.

        FINI - To finish; to be done with.

        FIX - 1. A dose of a drug.  2. To bribe.

        FLAG - A warning.

        FLATBACKER - A prostitute.

        FLATLINE - To kill.  A dead person or thing.

        FLETCHER - A flechette pistol, SMG, or rifle.

        FOUR-FIVE - A .45 caliber gun.

        FOXTROT UNIFORM - Fucked Up.

        FRAG - To kill, usually with explosives.

        FRY - To electrocute.

        GAP - To pull ahead of another rider/driver.

        GAT - A firearm.

        GEEK - To kill.

        GEISHA - (jap) Japan's professional female entertainers.

        GIRI - (jap) Closest translation is debt or obligation, but
        the concept entails much more.  Often used with the word "ninjo"
        by Yakuza to describe the basis for their 'honorable' traditions.

        GO LEO - To make a trip into Low Earth Orbit; ie, to visit
        one of the inner space stations.

        GOMI - (jap) Trash or garbage.

        GRAB GEE - To spend time in a gravity field.

        GRAV or GEE - 1. Gravity.  2. Weight.  3. A measure of importance.

        GRAVEROBBER - Someone who sells illicit body parts.

        GUMI - (jap) A suffix denoting association, company or gang,
        commonly used by both Yakuza groups and construction firms.

        GURENTAI - (jap) Ruffian or hoodlum.

        GYRO - Small one or two man helicopters, used mostly in police
        work and corporate strike operations.

        HAND CANNON - Any handgun in the 12mm and up range.

        HANDLE - A nickname; a working name you are known by on the street.

        HANGING PAPER - Passing bad checks.

        HARDFIRE - Streetslang for the Owari chemical trigger.

        HARD TIME - Jail time in state prison.

        HARNESS - A uniform.

        HEAD HUNTER - A female who does sexual acts for drugs.

        HEART - A liquid crystal matrix.

        HEAT - Police pressure.

        HEATER - A gun.

        HEATWAVE - A police crackdown.

        HIGH - To be on drugs.

        HIT - To kill.

        HOB - An international-style popular music, combining Western
        dance music with Afro/Arab and Asian rhythms, themes, and modes.

        HOLDING DOWN - Controlling turf or area.

        HOME PLATE - Your home or pad.

        HOOK UP - To get traction.

        HOSHO KAISHA - (jap) "Security Companies".  Hired muscle and
        rent-a-cops.

        HOTDOGGER - (derogatory) Inexperienced netrunners.

        HYDRO - Streetslang for hydrogen fuel, used to power a sizable
        number of vehicles in the 2000's.

        I.C.E. - Intrusion Countermeasure Electronics.  Programs that
        keep databases secure.

        ICEBREAKER - A program designed to overcome I.C.E..

        INPUT - Girlfriend.

        IN THE HUNT - (Motorcyclist) To be a strong contender.

        JAM - 1. To hurt.  2. To mess up.  3. To have sex with.

        -JOCKEY, -JOCK - A person with technical skills of a high order.

        JOHATSU - (jap) "The Disappeared People" or, literally,
        "evaporated".

        JOYBOY - Male prostitute.

        JOYGIRL - Female prostitute.

        KAI - (jap) A suffix denoting association or society, often used in
        gang names.

        KEYBOARD - Streetslang for a computer interface deck with manual
        keys.  Also, a terminal.

        KNIFE FIGHT - A hot and heavy fight with an enemy aircraft at
        close quarters.

        KOBUN - (jap) 1. "Child Role," used in conjunction with "oyabun"
        ("Parent Role") to connote the familial relationship within most
        Yakuza gangs. 2. Member of a Yakuza clan.

        KURUMAKU - (jap) Literally, black curtain, a term from traditional
        Kabuki theater.  Now used to denote a behind-the-scenes fixer,
        godfather, or powerbroker.

        L.A.M.A. - Los Angeles Metropolitan Access.

        LASSIE - A robohound.

        LEGIT - Legal.

        LINEFOOT - Nomad slang for anyone who isn't a nomad.

        LITEJACK - A type of popular music/performance art in which
        multiple instruments are played, through the Face, by one person.

        LIT UP - To be shot at.

        LIZ - A police patrol.

        L.P. - Lisenced Prostitute.  A legal prostitute.  Also called
        "Lolly Pops" by police.

        MAKE - 1. To obtain something.  2. To detect.

        MAKING BANK - To make money, usually illegally.

        MAN - Cop, policeman.

        MARK - (gang) A want-to-be gang member.

        MATCHBOX - A sleep cube or coffin.

        MAXIMUM, MAX - Good, superlative.

        MEATBALL - Someone augmented with grafted muscle.

        MINIMUM - Bad, sorrowful.

        MIZU SHOBAI - (jap) "Water Business" or "Water Trades", meaning
        nightclubs, bars, restaurants, and related businesses.

        MOLDED - Embarassed.

        MOTOR - (Motorcyclist) To outpower another rider.

        MOUTHPIECE - A lawyer.

        MR. JOHNSON - Refers to any anonymous employer or corporate agent.

        MUDBOY - (derogatory Oribital slang) An Earth man.

        MULE - 1. One who transports drugs.  2. A courier.

        NETRUN - To interface with the 'Net and use it to hack into Data
        Fortresses.

        NEUTRALIZE - Kill.  Assassinate.

        NINER - A nine millimeter gun.

        NINJO - (jap) Compassion or empathy.  Often used with "giri"
        obligation to describe Japanese conflict between one's duty and
        one's feelings; a central theme in Japanese literature.  Both
        are favorite terms of traditional Yakuza.

        NIPPERS - Handcuffs.

        N.O.E. - Nap-Of-the-Earth flying.  Flying as low as possible to
        avoid radar.

        ONE LARGE - A one hundred dollar bill.

        OUTPUT - Boyfriend.

        OVERCOOK - To go too fast.

        OVER THE SHOULDER - Any shoulder-mounted weapon.

        OYABUN - (jap) 1. "Parent Figure", used with kobun to describe
        the familial relationship within the gang.  Somewhat similar to
        the use of "godfather" in the West.  2. Head of a Yakuza clan.

        PACKIN' - To have a gun in your possession.

        PAD - Living quarters.

        PAINT BOYS - The Yakuza.

        PANZER - 1. An armored smuggling hovercraft.  2. Any ground effect
        combat vehicle.

        PANZERBOY - The driver of a panzer.

        PAPERHANGER - A counterfeit money passer.

        PASTA BOYS - The Mafia.

        PETER - A vault or safe.

        PETERMAN - A safecracker.

        PIG - A police officer.

        PIGEONS - Friendly aircraft.

        PIG ON A WHEEL - A motorcycle officer.

        PINCH - To arrest.

        PINEAPPLE - A bomb.

        PLASTIC - Fake; not real.

        PLAY DOUGH - Plastic explosives.

        PLUGGED IN - On life support.

        POLYMER ONE-SHOT - Any cheap, plastic pistol, usually in the five
        to six millimeter range.

        POP CAPS - To shoot at someone.

        POPSICLE - A frozen corpse, usually found in a drifting space wreck.

        POSERGANG - Any group whose members affect a specific look, or
        bodysculpt job.

        POST TIME - Time to start.

        PUKE - To blow an engine.

        PULL AN ASH - To give the wrong password or code.

        PULLING TEETH - Interrogating, esp. with torture.

        QUIFF - A prostitute.

        RABBI - A protector.

        RAD - 1. Radiation.  2. A dose of radiation.

        RAFFLES - A burglar.

        RAGS - Clothes.

        RAT - 1. To inform.  2. An informer.

        RECONFIG - To kill with a knife.

        RIN TIN TIN - A robohound, especially a police K9.

        RIPPERDOC - Surgeon specializing in implanting illegal cyberware.

        ROCKERBOY/GIRL - A musician or performer who uses his or her art
        to make political or social statements.  Rockerboys are not the same
        as "Rock Stars", who are usually "owned" by recording mediacorps
        and are apolitical.

        RONIN - (jap) 1. A freelance assassin or mercenary.  Usually
        considered to be untrustworthy.  2. A masterless samurai.

        ROUST - To be hassled by police.

        RUNNING THE LINE - Panzerboy slang for carrying contraband from
        one place to another.

        SAINT NICK - A benefactor.

        SAMURAI - (jap) 1. A corporate assassin or mercenary hired to
        protect corporate property or to make strikes against other corp-
        orate holdings.  2. Mercenary or muscle for hire.  Implies honor
        code.

        SARAKIN - (jap) "Salary man financiers," or more appropriately,
        loan sharks.

        SCREW - A prison guard.

        SETTLE - To kill.

        SHADES - Sunglasses.

        SHAIKUJIN - (jap) "Honest Citizen".  A corporate employee.

        SHANK - A knife.

        SHARK - A loan shark.

        SHOEMAKER - One who makes fake identification.

        SHOES - Fake identification.

        SIERRA HOTEL - Shit Hot.  A real pro.

        SING - To confess or inform on others.

        SITREP - Situation Report; how you are doing.

        SKIP - To leave.

        SLAMMIT ON - 1. To get violent. 2. To attack someone without reason.

        SO KA - (jap) I understand.

        SOKAIYA - (jap) "General Meeting Specialists," Japan's unique
        breed of financial racketeers.  Professional extortionists and
        strong-arm thugs who traditionally prey on shareholders meetings,
        but are now diversified into wide areas of organized crime.

        SOLAR WIND - Hot air, ie, something that is pretty much bullshit.

        SOUNDS - Music.

        SPILL - 1. To spend money.  2. To confess or inform on others.

        SQUEEZE - To put pressure on.

        SQUID - (Motorcyclist) An unskilled rider who rides too fast.

        THE STREET - Wherever you live, late at night.  The subculture,
        the underground.

        STUFFIT - 1. To have sex.  2. To forget something.

        SUCKER POCKETS - Pockets on the outside of garments.

        TAKE - The money a corrupt policeman takes, as in "on the take".

        TAKE A CAB - To leave.

        TAKE OUT - To murder.

        TEKIYA - (jap) Street stall operators and peddlers.

        THATCH - A type of psychotic killer.

        THIRDMAN - A middleman, often in the smuggler or criminal under-
        ground.

        THRASH - (Motorcyclist) To crash.

        THREADING THE NEEDLE - Flying through gaps in air defense radar.

        TORCH - To start a fire, usually arson.

        TORPEDO - A gunman or killer.

        TOYSTORE - Any place, legit or not, that deals in guns.

        TRAFFIC - (Motorcyclist) Groups of slower riders.

        TREY-EIGHT - A .38 caliber gun.

        TRIADS - Chinese organized crime syndicates.

        TRIPLE A - Anti-Aircraft Artillery.

        UNDER THE PAINT - (Motorcyclist) Tucking close to the motorcycle's
        gas tank to reduce wind resistance.

        UP ON IT - To have knowledge of the drug scene.

        USER INTERFACE - Anything used to snort, inject, or otherwise
        apply drugs.

        VENICE - Any part of a flooded coastal city.

        WALKABOUT - To go outside of a pressure dome or ship; to go EVA.

        WASHED - Refers to money that has been channeled through an
        intermediary to conceal it's source.

        WASTE - To kill.

        WEEFLE - (derogatory) An inexperienced netrunner.

        WETWORK - Assassination.

        WHIPLASH - A pulse laser.  So called because of the weapon's
        whip like crack when it is fired.

        WILSON - (derogatory) 1. Netrunner slang for someone who you
        consider stupid, crazy, or a screw-up.

        WIRE ROOM - A bookie's place.

        WISE GUYS - The Mafia.

        WRAITH - 1. A sniper.  2. A stealth aircraft.

        YUBITSUME - (jap) The ritual act within the Yakuza of slicing
        the joint off the little finger to atone for a mistake.

        ZEROED - To die.  To be killed.

        ZIP GUN - A homemade firearm.

        ZONEDANCE - Dancing turned into a dominance game.  The dancer tries
        to persuade, by charisma, talent, or violence, other dancers within
        his zone to conform to his movements.  Challengeing because other
        dancers are often listening to other music via cyberaudio.

"""


total = []
for ligne in text.splitlines() :
	if (ligne.count(" - ") == 1) :
		t = ligne.split(" - ")
		if len(t[0])>=2 :
			t[0] = t[0].replace("        ","")
			t[0] = t[0].replace(" ","_")
			total.append(t[0])

print total
print len(total)
needed = len(total)/4
needed = needed*4
print needed
i = 0
temp = []
while i < needed :
	des = random.randint(0,len(total)-1)
	temp.append(total[des])
	del[total[des]]
	i += 1
print temp
total = []
stotal = []
for t in temp :
	stotal.append(t)
	if (len(stotal) == needed/4):
		total.append(stotal)
		stotal = []
print total
for t in total :
	print t
	#print len(t)