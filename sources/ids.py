
MY_USER_ID = 194537964657704960
HERMIT_USER_ID = 244238135595106305

LAPROS_USER_ID = 785222129061986304
LAPROS_BETA_USER_ID = 768554429305061387
BOT_USER_IDS = [LAPROS_USER_ID, LAPROS_BETA_USER_ID]

class TEST:
    ID = 798023066718175252

    class CHANNEL:
        TEST = 799830678912499752
    
    class ROLE:
        MOD = 804128653687783424

class PWU:
    ID = 546872429621018635

    class CHANNEL:
        MISC = 546881598189207583
        HUMOR = 547580983860396051
    
    class ROLE:
        MOD = 550518609714348034
        JOKE_OWNER = 826971344834265128
    
    class EMOTE:
        AGONIZED_AXEW = "<:AgonizedAxew:698049607862714428>"
        LAUGHING_HENRY = "<:LaughingHenry:714352502358802455>"
        SEAN_DAB = "<:SeanDab:777619661285621774>"
        ANGRY_SLINK = "<:AngrySlink:749492163015999510>"
        ZANGOOSE_HUG = "<:ZangooseHug:731270215870185583>"

logChannelIDs = {
    TEST.ID: 804124151299178537,
    PWU.ID: 804087913272705025
}

MOD_ROLE_IDS = [PWU.ROLE.MOD, TEST.ROLE.MOD]
SHITPOST_CHANNELS = [
    TEST.CHANNEL.TEST,
    PWU.CHANNEL.MISC, PWU.CHANNEL.HUMOR
]