import numpy as np
import pandas as pd

#To Fix - TMs/Tutor Moves - Currently bugged because the extra moves not listed as a Move Tutor move is being registered as a TM move (Leading to some TM-blank in the wiki. Not really a big deal for now)

#This gets all the forms in the montext. There are a few forms that are filtered out (Darkrai's Various Puppet Master forms, Arceus' forms, Rift Forms, etc.) These exceptions will probably need updating as the game continues

encFile = open('RBFiles/montext.rb', "r", encoding='utf8')
tutorData = pd.read_csv('RBFiles/RejuvTutors.csv')
allLines = encFile.readlines()

tutorData.sort_values(by=['Location', 'UpperMove'])
tutorMoveNames = tutorData['UpperMove'].tolist()

def getGenderRatio(curLine):
    if(curLine.find("FemHalf") != -1):
        return 'Female50Percent'
    if(curLine.find("FemQuarter") != -1):
        return 'Female25Percent'
    if(curLine.find("FemEighth") != -1):
        return 'FemaleOneEighth'
    if(curLine.find("MaleQuarter") != -1):
        return 'Female75Percent'
    if(curLine.find("MaleEighth") != -1):
        return 'MaleOneEighth' #Check Litleo
    if(curLine.find("MaleZero") != -1):
        return 'AlwaysFemale'
    if(curLine.find("FemZero") != -1):
        return 'AlwaysMale'
    if(curLine.find("Genderless") != -1):
        return 'Genderless'
    else:
        return 'ToDoGender, '

def getEvolutionString(curLine):
    curLine = curLine.split(",")
    tmpHold = ''
    for i in range(len(curLine)):
        if(curLine[i] == ''):
            continue
        tmpHold += '"' + curLine[i] +'",'
    return tmpHold[:-1]

def getLevelMove(curLine):
    if(curLine == ''):
        return '[\'No Move\'], '
    else:
        curLine = curLine.split(',')
        return str(curLine[0])  + ',"' + curLine[1] + '"'
    return

def levelMoveText(moveList, ogMoveList):
    tmptext = ''
    if(len(moveList) == 0 and len(ogMoveList) == 0):
        return '[\'No Moves\']'
    elif(len(moveList) == 0):
        moveList = ogMoveList
    for curMove in moveList:
        tmptext += '\t\t\t' + curMove + ',\n'
    tmptext = tmptext[:-2]
    return tmptext

def eggMoveText(eggMoveList):
    eggMoveList = eggMoveList.replace(':', '')
    eggMoveList = eggMoveList.replace(' ', '')
    eggMoveList = eggMoveList.replace(']', '')
    eggMoveList = eggMoveList.replace('[', '')
    if(len(eggMoveList) < 5):
        return '' #No Egg moves (not a first stage evo, etc)
    allEggMoves = eggMoveList.split(",")
    tmpText = ''
    for curEggMoves in range(len(allEggMoves)):
        tmpText += '"' + allEggMoves[curEggMoves] + '",'
    tmpText = tmpText[:-1]
    #tmpText += ''
    return tmpText

def getGrowth(curLine):
    if(curLine == ''):
        return ''
    if(curLine.find('MediumSlow') != -1):
        return 'Parabolic'
    if(curLine.find('MediumFast') != -1):
        return 'Medium'
    return curLine

def getFormName(curLine, curName): #Prefixes and suffixes for pokemon names (Mega-, Giga-, (Alolan), etc)
    curName = curName.capitalize()
    if(curName == 'Mrmime'):
        curName = 'Mr. Mime'
    valid = True
    megState = False
    pre = ''
    suf = ''
    region = ''

    #To Check: Delpha, Goomink, Partner Pika/Eevee

    #Time to filter the non valid forms
    #Master of Nightmares
    if(curLine.find("Hand of") != -1 or curLine.find("Master") != -1 or curLine.find("Nightmare Remix") != -1):
        validForm = False
        return curLine, False, False, region 
    #Gardevoir
    if(curLine.find("Dark Gardevoir") != -1 or curLine.find("Angel of Death") != -1 or curLine.find("Fallen Angel") != -1):
        validForm = False
        return curLine, False, False, region 
    #ANA
    if(curLine.find("Nanodrive") != -1):
        validForm = False
        return curLine, False, False, region 
    #Talon
    if(curLine.find("Karma Beast") != -1):
        validForm = False
        return curLine, False, False, region 

    #General Rift Forms
    if(curLine.find("Rift ") != -1):
        validForm = False
        return curLine, False, False, region 
    if(curLine.find("Pulse+") != -1):
        validForm = False
        return curLine, False, False, region 
    
    #EV Meltans
    if(curName == "Meltan"):
        validForm = False
        return curLine, False, False, region 
    
    #Bots
    if(curLine.find("Amalgamation") != -1):
        validForm = False
        return curLine, False, False, region 
    
    #Regirock/Regice
    if(curLine.find("Guardian") != -1):
        validForm = False
        return curLine, False, False, region 

    #Individual Bosses
    if(curLine.find("Monstrosity") != -1):
        validForm = False
        return curLine, False, False, region 
    if(curLine.find("Tuff Puff") != -1):
        validForm = False
        return curLine, False, False, region 
    if(curLine.find("Kawopudunga") != -1):
        validForm = False
        return curLine, False, False, region 
    if(curLine.find("Dexoy") != -1):
        validForm = False
        return curLine, False, False, region 
    #Frosslass
    if(curLine.find("Released") != -1):
        validForm = False
        return curLine, False, False, region 
    if(curLine.find("Big Betty") != -1):
        validForm = False
        return curLine, False, False, region 
    if(curLine.find("Coffee Gregus") != -1):
        validForm = False
        return curLine, False, False, region 
    #Gothitelle
    if(curLine.find("Crescent's") != -1):
        validForm = False
        return curLine, False, False, region 
    
    #End Filter, start form name fixes
    #Darmanitan and Urshifu takes Priority cause of how its forms work
    if(curName == 'Darmanitan'):
        valid = True
        if(curLine.find('Galarian') != -1):
            region = '"Galarian"'
            pre = '"Galarian '
            if(curLine.find('Zen') != -1):
                pre += 'Zen Mode"'
            else:
                pre += 'Darmanitan"'
        elif(curLine.find('Zen') != -1):
            pre = '"Zen Mode"'
        else:
            pre = '"Darmanitan (Special)"'
        return pre, valid, megState, region
    if(curName == 'Urshifu'):
        valid = True
        if(curLine.find('Rapid') != -1):
            pre = '"Rapid Strike '
        else:
            pre = '"Single Strike '
        if(curLine.find('Giga') != -1):
            megState = True
            pre += 'Mega ' + curName + '"'
        else:
            pre += 'Style"'
        return pre, valid, megState, region

    if(curLine.find("Mega") != -1):
        valid = True
        megState = True
        pre = 'Mega '
        if(curLine.find("X") != -1):
            suf = ' X'
        elif(curLine.find("Y") != -1):
            suf = ' Y'
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Giga") != -1):
        megaGigaList = ['Venusaur', 'Charizard', 'Blastoise', 'Gengar']
        valid = True
        megState = True
        pre = 'Mega '
        if curName in megaGigaList:
            suf = ' G'
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Primal") != -1):
        valid = True
        megState = True
        pre = 'Primal '
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Origin") != -1):
        valid = True
        return curLine, valid, megState, region
    if(curLine.find("Eternamax") != -1):
        valid = True
        return curLine, valid, megState, region
    if(curLine.find("Zombie") != -1):
        valid = True
        pre = 'Aevian Zombie '
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Alolan") != -1):
        valid = True
        region = '"Alolan"'
        pre = 'Alolan '
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Galarian") != -1):
        valid = True
        region = '"Galarian"'
        pre = 'Galarian '
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Hisuian") != -1):
        valid = True
        region = '"Hisuian"'
        pre = 'Hisuian '
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Aevian") != -1):
        valid = True
        region = '"Aevian"'
        pre = 'Aevian '
        if(curName == 'Shellos' or curName == 'Gastrodon'):
            if(curLine.find('West') != -1):
                pre = 'West Aevian '
            else:
                pre = 'East Aevian '
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Female") != -1):
        valid = True
        suf = ' Female'
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Male") != -1):
        valid = True
        suf = ' Male'
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Therian") != -1):
        valid = True
        suf = 'Therian Forme'
        return ('"' + suf + '"'), valid, megState, region
    if(curLine.find("Dominant Fusion") != -1):
        valid = True
        suf = ' Dominant Fusion'
        return ('"' + pre + curName + suf + '"'), valid, megState, region
    if(curLine.find("Small") != -1):
        valid = True
        return '"Small Size"', valid, megState, region
    if(curLine.find("Unbound") != -1):
        valid = True
        return '"Unbound Forme"', valid, megState, region
    if(curName == 'Lycanroc'):
        valid = True
        return curLine, valid, megState, region
    if(curName == 'Zygarde'):
        valid = True
        if(curLine.find('10%') != -1):
            return '"10%"', valid, megState, region
        elif(curLine.find('Complete') != -1):
            return '"100%"', valid, megState, region
    if(curName == 'Necrozma'):
        valid = True
        if(curLine.find('Ultra') != -1):
            return '"Ultra"', valid, megState, region
        else:
            return curLine, valid, megState, region
    if(curName == 'Toxtricity'):
        if(curLine.find('Low Key') != -1):
            valid = True
            return '"Low Key"', valid, megState, region
    #The Weird and Wonderful
    if(curName == 'Gastrodon'): #No need for double normal Gastrodon
        valid = False
        if(curLine.find('West') != -1):
            return '"West Sea"', valid, megState, region
        else:
            return '"East Sea"', valid, megState, region
    
    
    directFormList = ['Castform', 'Deoxys', 'Wormadam', 'Rotom', 'Shaymin', 'Basculin', 'Kyurem', 'Meloetta', 'Aegislash', 'Oricorio', 'Wishiwashi', 'Minior', 'Eiscue', 'Morpeko', 'Zacian', 'Zamazenta', 'Calyrex']
    if(curName in directFormList): #Forms where the form name just directly translates
        valid = True
        return curLine, valid, megState, region
    
    if(curLine.find("Augmented") != -1): #Maybe?
        valid = False
        return '"Delpha"', valid, megState, region
    if(curLine.find("Goomink") != -1): #Maybe?
        valid = False
        return curLine, valid, megState, region
    if(curLine.find("Partner") != -1):
        valid = True
        return '"Partner ' + curName + '"', valid, megState, region
    if(curLine.find("Normal") != -1):
        pre = ''
        suf = ''
        return ('"' + pre + curName + suf + '"'), valid, megState, region

    suf = ' (Special)'
    return ('"' + pre + curName + suf + '"'), valid, megState, region

fullArray = '--List of information about each Pokemon\'s Forms, used to supplement the Species file.\n\n'
fullArray += 'local Forms = {\n'

changed = False

type1 = ''
type2 = ''

pokNum = 0
numForm = 0

baseStats = []
evs = ''
baseExp = ''

abilities = ''
hiddenAbility = ''

gendRate = ''

preEvoState = False
preEvoAll = ['', '']

evoState = False
evoPok = []

height = 0
weight = 0

wildItems = ['', '', '']

color = ''

levelMoveState = False
ogMoveList = []
moveList = []

compatibleState = False

eggSteps = ''
eggMoveList = ''
eggGroupsText = ''

kindText = ''
dexEntry = ''

formEnded = False
formAmount = 0
formNames = []
curFormName = ''
curForm = 0

prevPokNum = ''
newPok = False

validForm = True
megaForm = False
regionCode = ''

moveExceptionNames = ['CATERPIE', 'METAPOD', 'WEEDLE', 'KAKUNA', 'MAGNEMITE', 'MAGNETON', 'VOLTORB', 'ELECTRODE', 'STARYU', 'STARMIE', 'MAGIKARP', 'MAGIKARP', 'DITTO', 'PORYGON', 'ARTICUNO', 'ZAPDOS', 'MOLTRES', 'MEWTWO', 'MEW', 'UNOWN', 'WOBBUFFET', 'PORYGON2', 'SMEARGLE', 'RAIKOU', 'ENTEI', 'SUICUNE', 'LUGIA', 'HOOH', 'CELEBI', 'WURMPLE', 'SILCOON', 'CASCOON', 'NINCADA', 'NINJASK', 'SHEDINJA', 'LUNATONE', 'SOLROCK', 'WYNAUT', 'BELDUM', 'METANG', 'METAGROSS', 'REGIROCK', 'REGICE', 'REGISTEEL', 'KYOGRE', 'GROUDON', 'RAYQUAZA', 'JIRACHI', 'DEOXYS', 'KRICKETOT', 'BURMY', 'COMBEE', 'BRONZOR', 'BRONZOR', 'BRONZONG', 'BRONZONG', 'MAGNEZONE', 'PORYGONZ', 'ROTOM', 'ROTOM', 'ROTOM', 'UXIE', 'MESPRIT', 'AZELF', 'DIALGA', 'PALKIA', 'REGIGIGAS', 'GIRATINA', 'PHIONE', 'MANAPHY', 'DARKRAI', 'SHAYMIN', 'ARCEUS', 'VICTINI', 'KLINK', 'KLANG', 'KLINKLANG', 'TYNAMO', 'CRYOGONAL', 'GOLETT', 'GOLURK', 'COBALION', 'TERRAKION', 'VIRIZION', 'RESHIRAM', 'ZEKROM', 'KYUREM', 'KELDEO', 'MELOETTA', 'GENESECT', 'SCATTERBUG', 'SPEWPA', 'CARBINK', 'XERNEAS', 'YVELTAL', 'ZYGARDE', 'DIANCIE', 'HOOPA', 'VOLCANION', 'PIKIPEK', 'TRUMBEAK', 'TOUCANNON', 'PYUKUMUKU', 'TYPENULL', 'SILVALLY', 'KOMALA', 'DRAMPA', 'DHELMISE', 'TAPUKOKO', 'TAPULELE', 'TAPUBULU', 'TAPUFINI', 'COSMOG', 'COSMOEM', 'SOLGALEO', 'LUNALA', 'NIHILEGO', 'BUZZWOLE', 'PHEROMOSA', 'XURKITREE', 'CELESTEELA', 'KARTANA', 'GUZZLORD', 'NECROZMA', 'MAGEARNA', 'MARSHADOW', 'POIPOLE', 'NAGANADEL', 'STAKATAKA', 'BLACEPHALON', 'ZERAORA', 'MELTAN', 'MELMETAL', 'BLIPBUG', 'APPLIN', 'SINISTEA', 'POLTEAGEIST', 'FALINKS', 'DRACOZOLT', 'ARCTOZOLT', 'DRACOVISH', 'ARCTOVISH', 'ZACIAN', 'ZAMAZENTA', 'ETERNATUS', 'ZARUDE', 'REGIELEKI', 'REGIDRAGO', 'GLASTRIER', 'SPECTRIER', 'CALYREX', 'IRONMOTH']

moveExceptionMoves = [['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['BLASTBURN', 'DRACOMETEOR', 'DRAGONASCENT', 'FIREPLEDGE', 'FRENZYPLANT', 'GRASSPLEDGE', 'HYDROCANNON', 'RELICSONG', 'SECRETSWORD', 'STEELBEAM', 'WATERPLEDGE'], ['ATTRACT', 'BIDE', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'NATURALGIFT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['FACADE'], ['FACADE'], ['FACADE'], ['FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'RETURN', 'ROUND', 'SECRETPOWER', 'SNORE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['REST'], ['SWAGGER'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'DOUBLETEAM'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'BIDE', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'BIDE', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'FACADE'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'SWAGGER'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'FACADE', 'SLEEPTALK', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'DOUBLETEAM', 'SWAGGER'], ['ATTRACT', 'CAPTIVATE', 'SWAGGER'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'SWAGGER'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'SWAGGER'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE', 'CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['CONFIDE', 'DOUBLETEAM', 'ENDURE', 'FACADE', 'FRUSTRATION', 'HIDDENPOWER', 'NATURALGIFT', 'PROTECT', 'REST', 'RETURN', 'ROUND', 'SECRETPOWER', 'SLEEPTALK', 'SNORE', 'SUBSTITUTE', 'SWAGGER', 'TOXIC'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE'], ['ATTRACT', 'CAPTIVATE']]

universalMovesTMs = ['Attract', 'Confide', 'DoubleTeam', 'Facade', 'Frustration', 'HiddenPower', 'Protect', 'Rest', 'Return', 'Round', 'SecretPower', 'SleepTalk', 'Substitute', 'Swagger', 'Toxic']

universalMovesTutor = ['Bide', 'Captivate', 'Endure', 'NaturalGift', 'Snore', ]

def getTMsTutors(name, compMoveList):
    tutors = '\t\t["Tutor"]={'
    tms = '\t\t["TMs"]={'
    for k in range(len(universalMovesTMs)):
        if(name in moveExceptionNames):
            pokExceptionList = moveExceptionMoves[moveExceptionNames.index(name)]
            if(universalMovesTMs[k].upper in pokExceptionList):
                continue
            else:
                tms += '"' + universalMovesTMs[k].upper() + '",'
            continue
        else:
            tms += '"' + universalMovesTMs[k].upper() + '",'
    for k in range(len(universalMovesTutor)):
        if(name in moveExceptionNames):
            pokExceptionList = moveExceptionMoves[moveExceptionNames.index(name)]
            if(universalMovesTutor[k].upper in pokExceptionList):
                continue
            else:
                tutors += '"' + universalMovesTutor[k].upper() + '",'
            continue
        else:
            tutors += '"' + universalMovesTutor[k].upper() + '",'
    for k in range(len(compMoveList)):
        if(compMoveList[k] == ''):
            continue
        if(compMoveList[k] in tutorMoveNames):
            tutors += '"' + compMoveList[k] + '",'
        else:
            tms += '"' + compMoveList[k] + '",'
    tms = tms[:-1] + '},\n'
    tutors = tutors[:-1] + '},\n'
    return tms+tutors

for line in allLines:
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    if(len(line) == 0):
        continue
    if(line[0] == ':' and line[-1] == "{" and line.find('preevo') == -1 and line.find('MegaForm') == -1 and line.find('OnCreation') == -1 and line.find('URSHIFITE') == -1):
        #Skip the first pokemon. Will need to deal with the last pokemon at the end of the file
        if(pokNum == 0):
            pokNum += 1
            name = line[1:-5]
            continue
        
        if(changed):
        #Add to fullArray to write to file
            if not named:
                fullArray += '},\n["' + name + '"] = {\n'
                named = False
            fullArray += '\t{\n'
            fullArray += '\t\t["FormName"] = ' + curFormName + ',\n'
            if(regionCode != ''):
                    fullArray += '\t\t["Regional"]=' + regionCode + ',\n'
            if(type1 != ''):
                fullArray += '\t\t["Type1"]="' + type1 + '",\n'
            if(type2 != ''):
                fullArray += '\t\t["Type2"]="' + type2 + '",\n'
            
            if(abilities != ''):
                fullArray += '\t\t["Abilities"]={' + abilities + '},\n'
            if (hiddenAbility != ''):
                fullArray += '\t\t["HiddenAbility"]=' + hiddenAbility + ',\n'

            if(len(moveList) != 0):
                fullArray += '\t\t["Moves"]={'
                for i in range(len(moveList)):
                    fullArray += moveList[i] + ','
                fullArray = fullArray[:-1]
                fullArray += '},\n'
            
            if(baseStats != ''):
                fullArray += '\t\t["BaseStats"]=' + baseStats + '\n' #Comma already in text
            if(evs != ''):
                fullArray += '\t\t["EffortPoints"]=' + evs + '\n' #Comma already in text
            if(baseExp != ''):
                fullArray += '\t\t["BaseEXP"]=' + baseExp + ',\n'
            if(growthRate != ''):
                fullArray += '\t\t["GrowthRate"]="' + growthRate + '",\n'
            
            if(baseHappy != ''):
                fullArray += '\t\t["Happiness"]=' + baseHappy + ',\n'
            if(catchRate != ''):
                fullArray += '\t\t["Rareness"]=' + catchRate + ',\n' #Catchrate is called Rareness
            if(gendRate != ''):
                fullArray += '\t\t["GenderRate"]="' + gendRate + '",\n'
            
            if(height != ''):
                fullArray += '\t\t["Height"]=' + height + ',\n'
            if(weight != ''):
                fullArray += '\t\t["Weight"]=' + weight + ',\n'
            if(color != ''):
                fullArray += '\t\t["Color"]=' + color + ',\n'

            if(eggSteps != ''):
                fullArray += '\t\t["StepsToHatch"]=' + eggSteps + ',\n'
            if(eggMoveList != ''):
                fullArray += '\t\t["EggMoves"]={' + eggMoveList + '},\n'
            if(eggGroupsText != ''):
                fullArray += '\t\t["Compatibility"]={' + eggGroupsText + '},\n'

            if(kindText != ''):
                fullArray += '\t\t["Kind"]=' + kindText + ',\n'
            if(dexEntry != ''):
                fullArray += '\t\t["Pokedex"]="' + dexEntry + '",\n'

            if(wildItems[0] != ''):
                fullArray += '\t\t["WildItemCommon"]="' + wildItems[0] + '",\n'
            if(wildItems[1] != ''):
                fullArray += '\t\t["WildItemUncommon"]="' + wildItems[1] + '",\n'
            if(wildItems[2] != ''):
                fullArray += '\t\t["WildItemRare"]="' + wildItems[2] + '",\n'
            
            #Adding TMs & Tutors
            if(len(compList) > 0):
                fullArray +=  getTMsTutors(name, compList)

            if(preEvoAll[0] != ''):
                fullArray += '\t\t["PreEvolutions"]={"' + preEvoAll[0] + '",' + preEvoAll[1] + '},\n'

            if(len(evoPok) != 0):
                fullArray += '\t\t["Evolutions"]={'
                for j in range(len(evoPok)):
                    fullArray += evoPok[j] + ','
                fullArray = fullArray[:-1] + '},\n'
            else:
                fullArray += ''

            fullArray += "\t},\n"

        #Data Reset. Probably should make this a seperate function, but oh well
        type1 = ''
        type2 = ''
        abilities = ''
        hiddenAbility = ''

        moveList = []

        baseStats = ''
        evs = ''
        baseExp = ''
        growthRate = ''

        baseHappy = ''
        catchRate = ''
        gendRate = ''

        height = ''
        weight = ''
        color = ''

        eggSteps = ''
        eggMoveList = ''
        eggGroupsText = ''

        kindText = ''
        dexEntry = ''

        wildItems = ['', '', '']

        preEvoAll = ['', '']
        evoPok = []

        formEnded = False
        formAmount = 0
        formNames = []
        regionCode = ''
        #Finish reset, get the new Pokemon name
        name = line[1:-5]
        pokNum += 1
        changed = False
        newPok = False
        named = False
        continue
    if(line[0] == '"'):
        if(formAmount > 1):
            if(changed):
                if(pokNum!=3 and not newPok): #venusaur is the first different form
                    fullArray += '},\n'
                if(pokNum != prevPokNum):
                    fullArray += '["' + name + '"] = {\n'
                    named = True
                    newPok = True
                    prevPokNum = pokNum
                fullArray += '\t{\n'
                fullArray += '\t\t["FormName"] = ' + curFormName + ',\n'
                if(regionCode != ''):
                    fullArray += '\t\t["Regional"]=' + regionCode + ',\n'
                if(type1 != ''):
                    fullArray += '\t\t["Type1"]="' + type1 + '",\n'
                if(type2 != ''):
                    fullArray += '\t\t["Type2"]="' + type2 + '",\n'
                
                if(abilities != ''):
                    fullArray += '\t\t["Abilities"]={' + abilities + '},\n'
                if (hiddenAbility != ''):
                    fullArray += '\t\t["HiddenAbility"]=' + hiddenAbility + ',\n'

                if(len(moveList) != 0):
                    fullArray += '\t\t["Moves"]={'
                    for i in range(len(moveList)):
                        fullArray += moveList[i] + ','
                    fullArray = fullArray[:-1]
                    fullArray += '},\n'
                
                if(baseStats != ''):
                    fullArray += '\t\t["BaseStats"]=' + baseStats + '\n' #Comma already in text
                if(evs != ''):
                    fullArray += '\t\t["EffortPoints"]=' + evs + '\n' #Comma already in text
                if(baseExp != ''):
                    fullArray += '\t\t["BaseEXP"]=' + baseExp + ',\n'
                if(growthRate != ''):
                    fullArray += '\t\t["GrowthRate"]="' + growthRate + '",\n'
                
                if(baseHappy != ''):
                    fullArray += '\t\t["Happiness"]=' + baseHappy + ',\n'
                if(catchRate != ''):
                    fullArray += '\t\t["Rareness"]=' + catchRate + ',\n' #Catchrate is called Rareness
                if(gendRate != ''):
                    fullArray += '\t\t["GenderRate"]="' + gendRate + '",\n'
                
                if(height != ''):
                    fullArray += '\t\t["Height"]=' + height + ',\n'
                if(weight != ''):
                    fullArray += '\t\t["Weight"]=' + weight + ',\n'
                if(color != ''):
                    fullArray += '\t\t["Color"]=' + color + ',\n'

                if(eggSteps != ''):
                    fullArray += '\t\t["StepsToHatch"]=' + eggSteps + ',\n'
                if(eggMoveList != ''):
                    fullArray += '\t\t["EggMoves"]={' + eggMoveList + '},\n'
                if(eggGroupsText != ''):
                    fullArray += '\t\t["Compatibility"]={' + eggGroupsText + '},\n'

                if(kindText != ''):
                    fullArray += '\t\t["Kind"]=' + kindText + ',\n'
                if(dexEntry != ''):
                    fullArray += '\t\t["Pokedex"]="' + dexEntry + '",\n'

                if(wildItems[0] != ''):
                    fullArray += '\t\t["WildItemCommon"]="' + wildItems[0] + '",\n'
                if(wildItems[1] != ''):
                    fullArray += '\t\t["WildItemUncommon"]="' + wildItems[1] + '",\n'
                if(wildItems[2] != ''):
                    fullArray += '\t\t["WildItemRare"]="' + wildItems[2] + '",\n'

                #Add TMs & Tutor
                if(len(compList) > 0):
                    fullArray += getTMsTutors(name, compList)

                if(preEvoAll[0] != ''):
                    fullArray += '\t\t["PreEvolutions"]={"' + preEvoAll[0] + '",' + preEvoAll[1] + '},\n'

                if(len(evoPok) != 0):
                    fullArray += '\t\t["Evolutions"]={'
                    for j in range(len(evoPok)):
                        fullArray += evoPok[j] + ','
                    fullArray = fullArray[:-1] + '},\n'
                else:
                    fullArray += ''

                fullArray += "\t},\n"

        #More Resetting ahhhhhhhhhhhhhhhhhhh
        type1 = ''
        type2 = ''
        abilities = ''
        hiddenAbility = ''

        moveList = []
        compList = []

        baseStats = ''
        evs = ''
        baseExp = ''
        growthRate = ''

        baseHappy = ''
        catchRate = ''
        gendRate = ''

        height = ''
        weight = ''
        color = ''

        eggSteps = ''
        eggMoveList = ''
        eggGroupsText = ''

        kindText = ''
        dexEntry = ''

        wildItems = ['', '', '']

        preEvoAll = ['', '']
        evoPok = []
        regionCode = ''

        endLoc = line.find('=')
        curFormName = line[0:endLoc-1]
        curFormName, validForm, megaForm, regionCode = getFormName(curFormName, name) #Check if valid form and other stuff
        formAmount += 1
        changed = False
        formNames.append(curFormName)
        if(formAmount > 1):
            formEnded = True
    if(formAmount < 2 or not validForm):
        continue
    if(levelMoveState):
        ogLine = line
        if(line.find('#') != -1):
            continue
        line = line.replace(' ', '')
        line = line.replace(':', '')
        line = line.replace('[', '')
        line = line.replace(']', '')
        if(line.find('compatiblemoves') != -1):
            levelMoveState = False
            compatibleState = True
            startLoc = line.find('>')
            compList = line[startLoc+1:-1].replace(':', '')
            compList = compList.replace('[', '')
            compList = compList.replace(']', '')
            compList = compList.replace(' ', '')
            compList = compList.split(',')
            if(line.find(']') != -1):
                compatibleState = False
        if(line == '' or line == ','):
            levelMoveState = False
            continue
        moveList.append(getLevelMove(line))
        if(ogLine.find(']],') != -1):
            levelMoveState = False
        continue
    if(evoState):
        line = line.replace(' ', '')
        line = line.replace(':', '')
        line = line.replace('[', '')
        line = line.replace(']', '')
        if(line == '' or line == ','):
            evoState = False
            continue
        evoPok.append(getEvolutionString(line))
        continue
    if(preEvoState):
        if(line.find("species") != -1):
            startLoc = line.find('>',2)
            preEvoAll[0] = line[startLoc+2:-1].replace(":", '')
        if(line.find("form") != -1):
            startLoc = line.find('>',2)
            preEvoAll[1] = line[startLoc+2:]
        if(line.find("},") != -1):
            preEvoState = False
        continue
    if(compatibleState):
        if(line.find('#') != -1):
            continue
        tmpList = line.replace(':', '')
        tmpList = tmpList.replace('[', '')
        tmpList = tmpList.replace(']', '')
        tmpList = tmpList.replace(' ', '')
        tmpList = tmpList.split(',')
        compList = compList + tmpList
        compatibleState = False
        continue
    if(line.find('Type1 =>') != -1):
        startLoc = line.find('>', 0)
        line = line[startLoc+1:]
        startLoc = line.find(':', 0)
        type1 = line[startLoc+1:-1]
        changed = True
        continue
    if(line.find('Type2 =>') != -1):
        startLoc = line.find('>', 0)
        line = line[startLoc+1:]
        startLoc = line.find(':', 0)
        type2 = line[startLoc+1:-1]
        changed = True
        continue
    if(line.find('HiddenAbilities') != -1):
        startLoc = line.find('>',2)
        hiddenAbility = line[startLoc+2:-1].replace(":", '"') + '"'
        changed = True
        continue
    if(line.find('Abilities') != -1):
        startLoc = line.find('>')
        abilities = line[startLoc+1:-1]
        abilities = abilities.replace(" ", '')
        abilities = abilities.replace('[', '')
        abilities = abilities.replace(']', '')
        abilities = abilities.replace(":", '')
        abilitiesList = abilities.split(',')
        if(len(abilitiesList) == 3):
            hiddenAbility = '"' + abilitiesList.pop() + '"'
        abilities = ''
        for i in range(len(abilitiesList)):
            abilities += '"' + abilitiesList[i] + '",'
        abilities = abilities[:-1]
        changed = True
        continue
    if(line.find('BaseStats') != -1):
        baseStats = line.replace(" ", '')
        startLoc = baseStats.find('[')
        baseStats = baseStats.replace("[", '{')
        baseStats = baseStats.replace("]", '}')
        baseStats = baseStats[startLoc:]
        changed = True
        continue
    if(line.find('GrowthRate') != -1):
        startLoc = line.find('>')
        growthRate = line[startLoc+3:-1]
        growthRate = getGrowth(growthRate) #Convert MediumSlow to Parabolic and MediumFast to Medium (based on the previous file)
        changed = True
        continue
    if(line.find('BaseEXP') != -1):
        startLoc = line.find('>',2)
        baseExp = line[startLoc+2:-1]
        changed = True
        continue
    if(line.find('EVs') != -1): #EVs on the original file are not in the same order
        evs = line.replace(" ", '')
        startLoc = evs.find('[')
        evs = evs.replace("[", '{')
        evs = evs.replace("]", '}')
        evs = evs[startLoc:]
        changed = True
        continue
    if(line.find('CatchRate') != -1):
        startLoc = line.find('>',2)
        catchRate = line[startLoc+2:-1]
        changed = True
        continue
    if(line.find('EggSteps') != -1):
        startLoc = line.find('>',2)
        eggSteps = line[startLoc+2:-1]
        changed = True
        continue
    if(line.find('Happiness =>') != -1):
        startLoc = line.find('>',2)
        baseHappy = line[startLoc+2:-1]
        changed = True
        continue
    if(line.find('EggGroups') != -1):
        startLoc = line.find('[')
        endLoc = line.find(']')
        eggGroupsText = line[startLoc+1:endLoc]
        eggGroupsText = eggGroupsText.replace(":", '')
        commaLoc = eggGroupsText.find(',')
        if(commaLoc != -1 and len(eggGroupsText) > 0):
            eggGroupsText =  '"' + eggGroupsText[0:commaLoc] + '", "' + eggGroupsText[commaLoc+2:] + '"'
        else:
            eggGroupsText = '"' + eggGroupsText + '"'
        changed = True
        continue
    if(line.find("EggMoves") != -1):
        startLoc = line.find('>',2)
        tmpHold = line[startLoc+2:-1]
        eggMoveList = eggMoveText(tmpHold)
        changed = True
        continue
    if(line.find('dexentry') != -1):
        startLoc = line.find('>',2)
        tmpHold = line[startLoc+3:-2]
        tmpHold = tmpHold.replace('Poké', 'Poke') #multiple
        tmpHold = tmpHold.replace('“', '\'') #lake trio and probably others
        tmpHold = tmpHold.replace('”', '\'') #lake trio and probably others
        tmpHold = tmpHold.replace('º', ' degrees') #pansear degrees
        tmpHold = tmpHold.replace('—', '-') #skwovet and others’
        tmpHold = tmpHold.replace('’', '\'') 
        dexEntry = tmpHold
        changed = True
        continue
    if(line.find('kind =>') != -1):
        startLoc = line.find('>',2)
        kindText = line[startLoc+2:-1]
        changed = True
        continue
    if(line.find("Height =>") != -1):
        startLoc = line.find('>',2)
        height = line[startLoc+2:-1]
        #height = height[0:-1] + '.' + line[-1]
        height = '"' + str(float(float(height)/10)) + '"'
        changed = True
        continue
    if(line.find("Weight =>") != -1):
        startLoc = line.find('>',2)
        weight = line[startLoc+2:-1]
        weight = '"' + str(float(float(weight)/10)) + '"'
        changed = True
        continue
    if(line.find('Color =>') != -1):
        startLoc = line.find('>',2)
        color = line[startLoc+2:-1]
        #changed = True #Don't count as a change if this is the only one
        continue
    if(line.find('GenderRatio') != -1):
        startLoc = line.find('>',2)
        gendRate = getGenderRatio(line[startLoc+2:-1].replace(":", ''))
        changed = True
        continue
    if(line.find("WildItemCommon") != -1):
        startLoc = line.find('>',2)
        tmpHold = line[startLoc+2:-1]
        tmpHold = tmpHold.replace(':', '')
        if(len(wildItems) == 4):
            wildItems = ['', '', '']
        wildItems[0] = tmpHold
        changed = True
        continue
    if(line.find("WildItemUncommon") != -1):
        startLoc = line.find('>',2)
        tmpHold = line[startLoc+2:-1]
        tmpHold = tmpHold.replace(':', '')
        if(len(wildItems) == 4):
            wildItems = ['', '', '']
        wildItems[1] = tmpHold
        changed = True
        continue
    if(line.find("WildItemRare") != -1):
        startLoc = line.find('>',2)
        tmpHold = line[startLoc+2:-1]
        tmpHold = tmpHold.replace(':', '')
        if(len(wildItems) == 4):
            wildItems = ['', '', '']
        wildItems[2] = tmpHold
        changed = True
        continue
    if(line.find("Moveset") != -1):
        levelMoveState = True
        changed = True
        continue
    if(line.find("evolutions") != -1):
        if(line.find('[]') != -1):
            continue
        evoState = True
        evoPok = []
        changed = True
        continue
    if(line.find("preevo") != -1):
        preEvoState = True
        changed = True
        continue
    if(line.find(":compatiblemoves => ") != -1):
        compatibleState = True
        changed = True
        startLoc = line.find('>')
        compList = line[startLoc+1:-1].replace(':', '')
        compList = compList.replace('[', '')
        compList = compList.replace(']', '')
        compList = compList.replace(' ', '')
        compList = compList.split(',')
        if(line.find(']') != -1):
            compatibleState = False
        continue

# Don't worry about it! (Just dealing with the last Pokemon since we skipped the first one)
if(changed):
    fullArray += '["' + name + '"] = {\n'
    fullArray += 'ID=' + str(pokNum) + ',\n'
    if(type1 == ''):
        print(name + ' Something Went Wrong') #for any errors
    fullArray += 'Type1="' + type1 + '",\n'
    if(type2 != ''):
        fullArray += 'Type2="' + type2 + '",\n'

    fullArray += 'Abilities={' + abilities + '},\n'
    if (hiddenAbility != ''):
        fullArray += 'HiddenAbility=' + hiddenAbility + ',\n'

    if(len(moveList) == 0):
        print(name + ' moves went wrong')
    fullArray += 'Moves={'
    for i in range(len(moveList)):
        fullArray += moveList[i] + ','
    fullArray += '},\n'

    fullArray += 'BaseStats=' + baseStats + '\n' #Comma already in text
    fullArray += 'EffortPoints=' + evs + '\n' #Comma already in text
    fullArray += 'BaseEXP=' + baseExp + ',\n'
    fullArray += 'GrowthRate="' + growthRate + '",\n'

    fullArray += 'Happiness=' + baseHappy + ',\n'
    fullArray += 'Rareness=' + catchRate + ',\n' #Catchrate is called Rareness
    fullArray += 'GenderRate="' + gendRate + '",\n'

    fullArray += 'Height=' + height + ',\n'
    fullArray += 'Weight=' + weight + ',\n'
    fullArray += 'Color=' + color + ',\n'

    fullArray += 'StepsToHatch=' + eggSteps + ',\n'
    if(eggMoveList != ''):
        fullArray += 'EggMoves={' + eggMoveList + '},\n'
    fullArray += 'Compatibility={' + eggGroupsText + '},\n'

    fullArray += 'Kind=' + kindText + ',\n'
    if(dexEntry == ''):
        print(name + ' Empty Dex')
    fullArray += 'Pokedex="' + dexEntry + '",\n'

    if(wildItems[0] != ''):
        fullArray += 'WildItemCommon="' + wildItems[0] + '",\n'
    if(wildItems[1] != ''):
        fullArray += 'WildItemUncommon="' + wildItems[1] + '",\n'
    if(wildItems[2] != ''):
        fullArray += 'WildItemRare="' + wildItems[2] + '",\n'

    if(preEvoAll[0] != ''):
        fullArray += 'PreEvolutions={"' + preEvoAll[0] + '",' + preEvoAll[1] + '},\n'

    if(len(evoPok) != 0):
        fullArray += 'Evolutions={'
        for j in range(len(evoPok)):
            fullArray += evoPok[j] + ','
        fullArray = fullArray[:-1] + '},\n'
    else:
        fullArray += 'Evolutions={},\n'

    fullArray += 'FormAmount=' + str(formAmount) + ',\n' #How many forms

    fullArray += 'FormNames='
    for j in range(len(formNames)):
        fullArray += formNames[j] + ','
    fullArray += '\n'

    fullArray += "},\n"


fullArray += '},\n\n}\n\nreturn Forms'
newFile = open("Outputs/DatabaseForms.txt", "w")
newFile.write(fullArray)
newFile.close()
encFile.close()
#print(fullArray)