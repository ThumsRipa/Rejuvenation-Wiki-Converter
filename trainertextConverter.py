import numpy as np
import pandas as pd

trainerFile = open('RBFiles/trainertext.rb', "r", encoding='utf8')
#I manually edited line 15220 and 54609 (The whole xenogear section) from the file since it was inconsistent formatting with the rest of the data
trainerLines = trainerFile.readlines()

trainerTypes = pd.read_csv('RBFiles/trainerTypes.csv')
itemNames = pd.read_csv('RBFiles/itemNames.csv')
monNames = pd.read_csv('RBFiles/pokemonDexNums.csv')

curName = ''
curType = ''
curDifficulty = ''
trainerTypeString = ''
imageString = ''
items = ''
pokemonTime = False
monList = []
curMon = ['species', 'level', 'item', 'gender']
skip = True
started = False
form = ''

outputString = ''

for line in trainerLines:
    line = line.replace('\n', '')
    line = line.replace('\t', '')
    if(len(line) == 0):
        continue
    if(line.find('}]},') != -1):
        #Final Pokemon Save
        if(line.find(':ev') != -1):
            #do ev stuff
            line
        if(started):
            pokName = monNames.loc[monNames['CodeName'] == curMon[0]]['Name'].values[0]
            pokNum = str(monNames.loc[monNames['CodeName'] == curMon[0]]['DexNum'].values[0])
            while(len(pokNum) < 3):
                pokNum = '0' + pokNum
            if(form != ''):
                pokNum = pokNum + '_' + form
            if(curMon[2] == 'item'):
                pokItem = ''
            else:
                pokItem = itemNames.loc[itemNames['CodeName'] == curMon[2]]['Name'].values[0]
            if(curMon[3] == 'gender'):
                pokGender = 'B'
            else:
                pokGender = curMon[3]
            
            tempString = str(pokNum) + '|' + pokName + '|' + pokGender + '|' + curMon[1] + '|' + pokItem + '|'
            monList.append(tempString)
            curMon = ['species', 'level', 'item', 'gender']
        #end of trainer - make the line and reset
        finalLine = curType + '\n' + curName + '\n' + '{{Minor Trainers/entry|' + imageString + '|' + trainerTypeString + '|' + curName + '|Money|'
        #Number of Pokemon, Pokemon List
        finalLine += str(len(monList)) + '|'
        for monString in monList:
            if(len(monString) > 5):
                finalLine += monString
        finalLine += '36=' + items + '}}\n\n' #Items
        print(finalLine)
        outputString += finalLine
        monList = []
        items = ''
        skip = False
        pokemonTime = False
        continue
    if(line[0] == "#"):
        line = line.replace('\n', '')
        line = line.replace('\t', '')
        outputString += line + '\n'
    if(pokemonTime):
        #underscore under the number to indicate the form
        if(line.find(':species') != -1):
            line = line.replace('\n', '')
            line = line.replace(':', '')
            line  = line.replace(' ', '')
            startLoc = line.find('>')
            line = line[startLoc+1:-1]
            curMon[0] = line
        if(line.find(':form') != -1):
            line = line.replace('\n', '')
            line = line.replace(':', '')
            line  = line.replace(' ', '')
            startLoc = line.find('>')
            form = line[startLoc+1:-1]
        if(line.find(':level') != -1):
            line = line.replace('\n', '')
            line = line.replace(':', '')
            line  = line.replace(' ', '')
            startLoc = line.find('>')
            line = line[startLoc+1:-1]
            curMon[1] = line
        if(line.find(':gender') != -1):
            line = line.replace('\n', '')
            line = line.replace(':', '')
            line  = line.replace(' ', '')
            startLoc = line.find('>')
            line = line[startLoc+2:-2]
            curMon[3] = line
        if(line.find(':item ') != -1):
            line = line.replace('\n', '')
            line = line.replace(':', '')
            line  = line.replace(' ', '')
            startLoc = line.find('>')
            line = line[startLoc+1:-1]
            curMon[2] = line
        if(line.find('},') != -1):
            pokName = monNames.loc[monNames['CodeName'] == curMon[0]]['Name'].values[0]
            pokNum = str(monNames.loc[monNames['CodeName'] == curMon[0]]['DexNum'].values[0])
            while(len(pokNum) < 3):
                pokNum = '0' + pokNum
            if(form != ''):
                pokNum = pokNum + '_' + form
            if(curMon[2] == 'item'):
                pokItem = ''
            else:
                pokItem = itemNames.loc[itemNames['CodeName'] == curMon[2]]['Name'].values[0]
            if(curMon[3] == 'gender'):
                pokGender = 'B'
            else:
                pokGender = curMon[3]
            tempString = str(pokNum) + '|' + pokName + '|' + pokGender + '|' + curMon[1] + '|' + pokItem + '|'
            monList.append(tempString)
            curMon = ['species', 'level', 'item', 'gender']
        continue
    if skip:
        continue
    if(line.find(':items') != -1):
        startLoc = line.find('[')
        endLoc = line.find(']')
        origLine = line
        line = line[startLoc+1:endLoc]
        line = line.replace(':', '')
        line = line.split(',')
        if(len(line) == 0):
            continue
        items = ''
        for item in line:
            if(item == ''):
                items += ', '
                continue
            items += itemNames.loc[itemNames['CodeName'] == item]['Name'].values[0] + ', '
        items = items[:-2]
        continue
    if(line.find('teamid') != -1):
        started = True
        if(line.find("ALICEALLEN") != -1):
            skip = True
            continue
        startLoc = line.find('[')
        endLoc = line.find(']')
        origLine = line
        line = line[startLoc+1:endLoc]
        line = line.split(',')
        curName = line[0][1:-1]
        curType = line[1][1:]
        curDifficulty = line[2]
        trainerTypeString = trainerTypes.loc[trainerTypes['Code'] == curType]['Title'].values[0]
        imageString = trainerTypes.loc[trainerTypes['Code'] == curType]['Image'].values[0]
        continue
    if(line.find(':mons') != -1):
        pokemonTime = True
        form = ''
        continue

trainerFile.close()

newFile = open("Outputs/MinorTrainers.txt", "w", encoding="utf-8")
newFile.write(outputString)
newFile.close()