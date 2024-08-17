import numpy as np
import pandas as pd

#This is for if I am allowed to update the Encounter part in the Database lua. Should make it easier that trying to convert to the other version (hopefully)

#Note for whoever's doing this after me.
#Event Pokemon csv will need to be updated per version. I suggest using Google Sheets to compile everything and then download as csv to the folder

encFile = open('RBFiles/enctext.rb', "r", encoding='utf8')
monFile = open('RBFiles/montext.rb', "r", encoding='utf8')
eventFile = pd.read_csv('RBFiles/EventEncounters.csv')

#Start with the event Pokemons
eventText = '["Events"] = {\n'
formsEventText = '["FormEvents"] = {\n'
curPokName = ''
curFormName = ''

for i, j in eventFile.iterrows():
    #This bottom line won't check for NidoranF/NidoranM if there are more than 1 events for each of them.
    if(j['Pokemon'].replace(" ", "").replace("-", "").upper() == curPokName):
        eventText = eventText[:-3] + ', '
        #Working on the assumption that all trades will have "Any" or "N/A" time
        if(j['Time'] == 'Any' or j['Time'] == 'N/A'):
            timeText = ''
        else:
            timeText += ' (' + str(j['Time']) + ')'
        tempText = j['Location'] + timeText + ' (' + j['Method'] + ')'
        if(j['Method'] == "Trade"):
            tempText = tempText[:-1]
            tempText += ' ' + j['Notes'] + ')'
        eventText += tempText + '",\n'
        continue
    elif(j['Pokemon'].find('(') != -1):
        if(j['Pokemon'] == curFormName):
            formsEventText = formsEventText[:-3] + ', '
            #Working on the assumption that all trades will have "Any" or "N/A" time
            if(j['Time'] == 'Any' or j['Time'] == 'N/A'):
                timeText = ''
            else:
                timeText += ' (' + str(j['Time']) + ')'
            tempText = j['Location'] + timeText + ' (' + j['Method'] + ')'
            if(j['Method'] == "Trade"):
                tempText = tempText[:-1]
                tempText += ' ' + j['Notes'] + ')'
            formsEventText += tempText + '",\n'
            continue
        curFormName = j['Pokemon']
        curPokName = curFormName[0:(curFormName.find('(')-1)].upper()
        curPokName = curPokName.replace(" ", "")
        curPokName = curPokName.replace("-", "")
        timeText = ''
        if(j['Time'] == 'Any' or j['Time'] == 'N/A'):
            timeText = ''
        else:
            timeText += ' (' + str(j['Time']) + ')'
        tempText = j['Location'] + timeText + ' (' + j['Method'] + ')'
        if(j['Method'] == "Trade"):
            tempText = tempText[:-1]
            tempText += ' ' + j['Notes'] + ')'
        formsEventText += '\t["'+ curPokName +'"]="' + tempText + '",\n'
        #print('Form for ' + j['Pokemon'])
        continue
    curPokName = j['Pokemon']
    curPokName = curPokName.replace(" ", "")
    curPokName = curPokName.replace("-", "")
    curPokName = curPokName.upper()
    #Name Exceptions (Nidoran, Mostly)
    if(curPokName == 'NIDORANFEMALE'):
        curPokName = 'NIDORANfE'
    elif (curPokName == 'NIDORANMALE'):
        curPokName = 'NIDORANmA'
    timeText = ''
    if(j['Time'] == 'Any' or j['Time'] == 'N/A'):
        timeText = ''
    else:
        timeText += ' (' + str(j['Time']) + ')'
    tempText = j['Location'] + timeText + ' (' + j['Method'] + ')'
    if(j['Method'] == "Trade"):
        tempText = tempText[:-1]
        tempText += ' ' + j['Notes'] + ')'
    eventText += '\t["'+ curPokName +'"]="' + tempText + '",\n'
    #print(j["Pokemon"])

eventText += '},\n'
formsEventText += '},\n'

fullEventText = eventText + formsEventText

#print(fullEventText)

encLines = encFile.readlines()
monLines = monFile.readlines()

#Copy and Paste from System Constant file

#Alolan
Rattata = [55,58,59,91,144,194,209,218,24,82,390,391] #and aMeowth!
Sandshrew = [146,150,165,171,174,178,181,269,479,480,481,482,483,485,486,490,491]
Vulpix = []
Diglett = [97,116,403,404]
Geodude = [269,289,419,489,569]
Grimer = [64,66,138]
Cubone = []
# Galarian
MrMime = [75,146,150,165,171,174,178,181,269,470,471,479,480,481,482,483,485,486,490,491]
Darumaka = []
Meowth = [97,238] #gmeowth
Ponyta = [357,358,359,360,368]
Slowpoke = [474]
PonyShowMaps = []
Farfetchd = [201]
Zigzagoon = [12,95]
YamaskEvo = [11,12,489,508]
YamaskSpawn = [12,489,508]
Stunfisk = [201]
Corsola = [584]
# Hisui
Growlithe = [140,523]
Voltorb = [179,181]
Typhlosion = []
Qwilfish = [300]
Sneasel = [521]
Samurott = []
Lilligant = [7,15,30,127,131,202,206,254,273,285,315,419,423,424,425,426,]
Basculin = [395]
Zorua = [107,470]
Braviary = [75,146,150,165,171,174,178,181,269,470,471,479,480,481,482,483,485,486,490,491]
Sliggoo = [600,601,602]
Avalugg = [295]
Decidueye = []
# Aevian
Paras = [64]
Magikarp = [221]
Misdreavus = [201,371]
Shroomish = [357,358,359,360,361,368]
Feebas = [474]
Snorunt = [221,295]
Munna = [57,145] # Mellow mellow Munna!
Sigilyph = [458]
Litwick = [111]
Budew = [373,478,510,515,523,525]
Bronzor = [137,227,357,358,359,360,363,368,494,498,499]
AevShellos = [300,329,540]
Toxtricity = []
Jangmoo = []
Wimpod = [523]
Larvesta = []
Sewaddle = [254]
Mareep = []
Lapras = [109]

#Copy and paste the map list from above to make a dict
pokemonFormList = {'RATTATA': [55,58,59,91,144,194,209,218,24,82,390,391], 'MEOWTH': [97,238], 'SANDSHREW': [146,150,165,171,174,178,181,269,479,480,481,482,483,485,486,490,491], 'VULPIX': [], 'DIGLETT':[97,116,403,404], 'GEODUDE':[269,289,419,489,569], 'GRIMER': [64,66,138], 'CUBONE': [], 'MRMIME': [75,146,150,165,171,174,178,181,269,470,471,479,480,481,482,483,485,486,490,491], 'DARUMAKA': [], 'PONYTA': [357,358,359,360,368], 'SLOWPOKE': [474], 'FARFETCHD': [201], 'ZIGZAGOON': [12,95], 'YAMASK': [12,489,508], 'STUNFISK': [201], 'CORSOLA': [584], 'GROWLITHE': [140,523], 'VOLTORB': [179,181], 'TYPHLOSION': [], 'QWILFISH': [300], 'SNEASEL': [521], 'SAMUROTT': [], 'LILLIGANT': [7,15,30,127,131,202,206,254,273,285,315,419,423,424,425,426], 'BASCULIN': [395], 'ZORUA': [107,470], 'BRAVIARY': [75,146,150,165,171,174,178,181,269,470,471,479,480,481,482,483,485,486,490,491], 'SLIGGOO': [600,601,602], 'AVALUGG': [295], 'DECIDUEYE': [], 'PARAS': [64], 'MAGIKARP': [221], 'MISDREAVUS': [201, 371], 'SHROOMISH': [357,358,359,360,361,368], 'FEEBAS': [474], 'SNORUNT': [221, 295], 'MUNNA': [57,145], 'SIGILYPH': [458], 'LITWICK': [111], 'BUDEW': [373,478,510,515,523,525], 'BRONZOR': [137,227,357,358,359,360,363,368,494,498,499], 'SHELLOS': [300,329,540], 'TOXTRICITY': [], 'JANGMOO': [], 'WIMPOD': [523], 'LARVESTA': [], 'SEWADDLE': [254], 'MAREEP': [], 'LAPRAS':[109]}

keysList = list(pokemonFormList.keys())

#print(keysList)

def getRate(thisLine):
    rate = 0
    startLoc = thisLine.find('[[')
    endLoc = thisLine.find(']]')
    allNums = thisLine[startLoc+2:endLoc]
    allNums = allNums.replace('[', '')
    allNums = allNums.replace(']', '')
    allNums = allNums.split(',')
    for i in range(len(allNums)):
        if(i%3 == 0):
            if(allNums[i] == ''):
                continue
            rate += int(allNums[i])
    return rate

def checkForm(thisPok, thisMap):
    if(thisPok in keysList):
        thisMapList = pokemonFormList[thisPok]
        if(thisPok == 'MEOWTH'): #Meowth Exception
            thisMapList = pokemonFormList['RATTATA']
            if(thisMap in thisMapList):
                return 0
            thisMapList = pokemonFormList[thisPok]
            if(thisMap in thisMapList):
                return 1
        if(thisMap in thisMapList):
            return 0
    return -1 #Returns -1 for the pokemon being default form. Returns 0 for Form 1, 1 for Form 2, etc


mapNumber = ''
mapName = ''
encType = ''

mapList = []
formsMapList = []

pokName = ''
forms = False

fullText = '["Wild"]={\n'
shortText = ''
formsText = ''
formsShortText = ''
formsMultText = ['', ''] #Only max two forms needed for now, no other pokemon has more than 2 wild encounters form. It's just Meowth at the moment
start = True
startForms = True
found = False
foundForms = False

for line in monLines:
    line = line.replace('\n', '')
    if(len(line) == 0):
        continue
    if(line[0] == ':'):
        if(start):
            start = False
        else:
            if(found):
                fullText += shortText + '\t},\n'
        endLoc = line.find('=')
        pokName = line[1:endLoc-1]
        shortText = '\t["' + pokName + '"]={\n'

        if pokName in keysList:
            if(len(pokemonFormList[pokName]) > 0):
                forms = True
                if(startForms):
                    startForms = False
                else:
                    if(foundForms):
                        formsText += formsShortText
                        for thisLoop in range(len(formsMultText)):
                            if(formsMultText[thisLoop] != ''):
                                formsText += '\t\t["Form' + str(thisLoop+1) + '"]={\n' + formsMultText[thisLoop] + '\t\t},\n'
                        formsText += '\t},\n'
                formsShortText = '\t["' + pokName + '"]={\n'
                foundForms = False
                formsMultText = ['', '']
            else:
                forms = False
        else:
            forms = False

        #Start map hunting
        mapList = []
        formsMapList = []
        found = False
        

        for lineTwo in encLines:
            lineTwo = lineTwo.replace('\t', '')
            lineTwo = lineTwo.replace('\n', '')
            if(len(lineTwo) == 0):
                continue
            if(lineTwo.find('#') != -1):
                numberLoc = lineTwo.find('#')
                mapName = lineTwo[numberLoc+2:]
                mapName = mapName.replace('|', '-')
                while(mapName[-1] == ' '):
                    mapName = mapName[:-1]
                numberLoc = lineTwo.find('=')
                mapNumber = int(lineTwo[:numberLoc-1])

                #Special Map Names
                if(mapNumber == 571):
                    mapName = 'Gearen Park - Neo'
                elif(mapNumber == 71):
                    mapName = 'Route 3 - Goldenwood'
                elif(mapNumber == 67 or mapNumber == 69):
                    mapName = 'Route 3 - Sheridan'
                elif(mapNumber == 236):
                    mapName = 'Route 3 - Past'
                elif(mapNumber == 322):
                    mapName = 'Route 5 - Past'
                elif(mapNumber == 321):
                    mapName = 'Goldenwood Forest - Overgrown'
                
                elif(mapNumber == 139):
                    mapName = 'Valor Mountain - Neutral'
                elif(mapNumber == 140):
                    mapName = 'Valor Mountain - Fire'
                elif(mapNumber == 146):
                    mapName = 'Valor Mountain - Ice'
                continue
            
            #Get Encounter Type
            if(lineTwo[0] == ':' and lineTwo[-1] == '{'):
                numberLoc = lineTwo.find('=')
                encType = lineTwo[1:numberLoc-1]
                if(encType == 'Water'):
                    encType = 'Surfing'
                elif(encType == 'Land'):
                    encType = 'Grass'
                elif(encType == 'LandDay'):
                    encType = 'Grass [Day]'
                elif(encType == 'LandNight'):
                    encType = 'Grass [Night]'
                elif(encType == 'LandMorning'):
                    encType = 'Grass [Morning]'
                elif(encType == 'OldRod'):
                    encType = 'Old Rod'
                elif(encType == 'GoodRod'):
                    encType = 'Good Rod'
                elif(encType == 'SuperRod'):
                    encType = 'Super Rod'
                elif(encType == 'RockSmash'):
                    encType = 'Rock Smash'
                
            if(lineTwo.find(pokName) != -1):
                fullMapName = mapName + ' (' + encType + ')'
                pokRate = getRate(lineTwo)
                if(forms):
                    rightForm = checkForm(pokName, mapNumber)
                else:
                    rightForm = -1
                if((not (fullMapName in mapList)) and rightForm == -1):
                    shortText += '\t\t{"' + fullMapName + '", "' + str(pokRate) + '"},\n'
                    mapList.append(fullMapName)
                    found = True
                    continue
                elif((not (fullMapName in formsMapList)) and (not (rightForm == -1))):
                    formsMultText[rightForm] += '\t\t\t{"' + fullMapName + '", "' + str(pokRate) + '"},\n'
                    formsMapList.append(fullMapName)
                    foundForms = True
                    continue
                else:
                    continue
            continue

fullText += '},\n["Forms"]={\n'

fullText += formsText[:-1] + '\n'

fullText += '}\n'

actualFull = 'local Database = {\n' + fullEventText + fullText + '}\nreturn Database'


newFile = open("Outputs/DatabaseEncounters.txt", "w")
newFile.write(actualFull)
newFile.close()
encFile.close()
monFile.close()