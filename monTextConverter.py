import numpy as np
import pandas as pd

#This is the big one right here. This gets the base form of all the Pokemon, and all the extra forms are separately compiled in the monTextConvereter-Forms.py file. This is originally the PBS files had Species and Forms in separate files, but the RB files now has it all in one.

#One other thing that needs to be updated (As of Jan 2024) is that the evolutions currently don't have the form it evolves into marked. This is especially relevant for mons like Exeggcute where it only has a single evolution method for two different evolutions

encFile = open('RBFiles/montext.rb', "r", encoding='utf8')
allLines = encFile.readlines()

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
    
fullArray = '--List of information about each Pokemon, used to construct a variety of templates.\n\n'
fullArray += 'local Database = {\n'

type1 = ''
type2 = ''

pokNum = 0
numForm = 0

baseStats = []
evs = ''
baseExp = ''

abilities = []
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

compatibleMoveState = False

eggSteps = ''
eggMoveList = ''
eggGroupsText = ''

kindText = ''
dexEntry = ''

formEnded = False
formAmount = 0
formNames = []
curForm = 0

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
        
        #Add to fullArray to write to file
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
        #Finish reset, get the new Pokemon name
        name = line[1:-5]
        pokNum += 1
        continue
    if(line[0] == '"'):
        endLoc = line.find('=')
        curFormName = line[0:endLoc-1]
        #Check if valid form - For later
        formAmount += 1
        formNames.append(curFormName)
        if(formAmount > 1):
            formEnded = True
    if(formEnded):
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
            compatibleMoveState = True
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
    if(line.find('Type1 =>') != -1):
        startLoc = line.find('>', 0)
        line = line[startLoc+1:]
        startLoc = line.find(':', 0)
        type1 = line[startLoc+1:-1]
        continue
    if(line.find('Type2 =>') != -1):
        startLoc = line.find('>', 0)
        line = line[startLoc+1:]
        startLoc = line.find(':', 0)
        type2 = line[startLoc+1:-1]
        continue
    if(line.find('HiddenAbilities') != -1):
        startLoc = line.find('>',2)
        hiddenAbility = line[startLoc+2:-1].replace(":", '"') + '"'
        continue
    if(line.find('Abilities') != -1):
        startLoc = line.find('>')
        abilities = line[startLoc+1:-1]
        abilities = abilities.replace(" ", '')
        abilities = abilities.replace('[', '')
        abilities = abilities.replace(']', '')
        abilities = abilities.replace(":", '')
        abilitiesList = abilities.split(',')
        abilities = ''
        for i in range(len(abilitiesList)):
            abilities += '"' + abilitiesList[i] + '",'
        abilities = abilities[:-1]
        continue
    if(line.find('BaseStats') != -1):
        baseStats = line.replace(" ", '')
        startLoc = baseStats.find('[')
        baseStats = baseStats.replace("[", '{')
        baseStats = baseStats.replace("]", '}')
        baseStats = baseStats[startLoc:]
        continue
    
    if(line.find('GrowthRate') != -1):
        startLoc = line.find('>')
        growthRate = line[startLoc+3:-1]
        growthRate = getGrowth(growthRate) #Convert MediumSlow to Parabolic and MediumFast to Medium (based on the previous file)
        continue
    if(line.find('BaseEXP') != -1):
        startLoc = line.find('>',2)
        baseExp = line[startLoc+2:-1]
        continue
    if(line.find('EVs') != -1): #EVs on the original file are not in the same order
        evs = line.replace(" ", '')
        startLoc = evs.find('[')
        evs = evs.replace("[", '{')
        evs = evs.replace("]", '}')
        evs = evs[startLoc:]
        continue
    if(line.find('CatchRate') != -1):
        startLoc = line.find('>',2)
        catchRate = line[startLoc+2:-1]
        continue
    
    if(line.find('EggSteps') != -1):
        startLoc = line.find('>',2)
        eggSteps = line[startLoc+2:-1]
        continue
    if(line.find('Happiness =>') != -1):
        startLoc = line.find('>',2)
        baseHappy = line[startLoc+2:-1]
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
        continue
    if(line.find("EggMoves") != -1):
        startLoc = line.find('>',2)
        tmpHold = line[startLoc+2:-1]
        eggMoveList = eggMoveText(tmpHold)
        continue
    
    if(line.find('dexentry') != -1):
        startLoc = line.find('>',2)
        tmpHold = line[startLoc+3:-2]
        tmpHold = tmpHold.replace('Poké', 'Poke') #multiple
        tmpHold = tmpHold.replace('“', '\'') #lake trio and probably others
        tmpHold = tmpHold.replace('”', '\'') #lake trio and probably others
        tmpHold = tmpHold.replace('º', ' degrees') #pansear degrees
        tmpHold = tmpHold.replace('—', '-') #skwovet and others
        dexEntry = tmpHold
        continue
    if(line.find('kind =>') != -1):
        startLoc = line.find('>',2)
        kindText = line[startLoc+2:-1]
        continue
    if(line.find("Height =>") != -1):
        startLoc = line.find('>',2)
        height = line[startLoc+2:-1]
        height = '"' + str(float(float(height)/10)) + '"'
    if(line.find("Weight =>") != -1):
        startLoc = line.find('>',2)
        weight = line[startLoc+2:-1]
        weight = '"' + str(float(float(weight)/10)) + '"'
    if(line.find('Color =>') != -1):
        startLoc = line.find('>',2)
        color = line[startLoc+2:-1]
        continue
    if(line.find('GenderRatio') != -1):
        startLoc = line.find('>',2)
        gendRate = getGenderRatio(line[startLoc+2:-1].replace(":", ''))
        continue

    if(line.find("WildItemCommon") != -1):
        startLoc = line.find('>',2)
        tmpHold = line[startLoc+2:-1]
        tmpHold = tmpHold.replace(':', '')
        if(len(wildItems) == 4):
            wildItems = ['', '', '']
        wildItems[0] = tmpHold
        continue
    if(line.find("WildItemUncommon") != -1):
        startLoc = line.find('>',2)
        tmpHold = line[startLoc+2:-1]
        tmpHold = tmpHold.replace(':', '')
        if(len(wildItems) == 4):
            wildItems = ['', '', '']
        wildItems[1] = tmpHold
        continue
    if(line.find("WildItemRare") != -1):
        startLoc = line.find('>',2)
        tmpHold = line[startLoc+2:-1]
        tmpHold = tmpHold.replace(':', '')
        if(len(wildItems) == 4):
            wildItems = ['', '', '']
        wildItems[2] = tmpHold
        continue

    if(line.find("Moveset") != -1):
        levelMoveState = True
        continue
    if(line.find("evolutions") != -1):
        if(line.find('[]') != -1):
            continue
        evoState = True
        evoPok = []
        continue
    if(line.find("preevo") != -1):
        preEvoState = True

# Don't worry about it! (Just dealing with the last Pokemon since we skipped the first one)
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


fullArray += '}\n\nreturn Database'
newFile = open("Outputs/DatabaseSpecies.txt", "w", encoding="utf-8")
newFile.write(fullArray)
newFile.close()
encFile.close()
#print(fullArray)