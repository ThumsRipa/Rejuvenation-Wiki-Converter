import numpy as np
import pandas as pd

#RejuvTutors.csv needs to be manually updated as new Move Tutor moves get added

monFile = open('RBFiles/montext.rb', "r", encoding='utf8')
itemFile = open('RBFiles/itemtext.rb', "r", encoding='utf8')
tutorData = pd.read_csv('RBFiles/RejuvTutors.csv')
monLines = monFile.readlines()
itemLines = itemFile.readlines()

tutorData.sort_values(by=['Location', 'UpperMove'])

tutorMoveNames = tutorData['UpperMove'].tolist()
tutorMoveLoc = tutorData['Location'].tolist()
tutorMoveCondition = tutorData['Condition'].tolist()
allTutorMoves = []

for i in range(len(tutorMoveLoc)):
    if(tutorMoveCondition[i] == 'None' or tutorMoveCondition[i] == 'Akuwa Town Residents'):
        allTutorMoves.append([tutorMoveNames[i], tutorMoveLoc[i], "Tutor"])
    else:
        allTutorMoves.append([tutorMoveNames[i], tutorMoveLoc[i] + ', ' + tutorMoveCondition[i], "Tutor"])

def addToList(oldList, newList):
    for curMove in newList:
        if(curMove not in oldList and curMove != 'POUNCE'):
            oldList.append(curMove)
    return oldList

listedMoves = []
TMList = []
tmpList = []
tmNum = 0
tmName = ''
tmMove = ''
compState = False
tmNum = 1

curAdd = 0
maxTM = 157
maxRM = 9

for line in itemLines:
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    if(line.find(':TM') != -1):
        curAdd = 0
        #endLoc = line.find('=')
        #tmNum = int(line[3:endLoc-1])
    if(line.find(':HM') != -1):
        curAdd = maxTM + maxRM
        #tmNum = int(line[3:endLoc-1])
    if(line.find(':RM') != -1):
        curAdd = maxTM
    if(line.find(':name =>') != -1):
        startLoc = line.find('"')
        tmName = line[startLoc+1:-2]
    if(line.find(':tm =>') != -1):
        startLoc = line[2:].find(':')
        tmMove = line[startLoc+3:-1]
        tmNum = int(tmName[2:]) + curAdd
        if(tmNum == 110):
            TMList.append([109, "???", "TM109"])
        TMList.append([tmNum, tmMove, tmName])
        tmNum += 1

TMList.sort(key = lambda a: a[0])

availableMoveList = TMList + allTutorMoves
#print(availableMoveList)

availableMoveListNames = []
for i in range(len(availableMoveList)):
    if(i < 171): #TMs & HMs
        availableMoveListNames.append(availableMoveList[i][1])
    else:
        availableMoveListNames.append(availableMoveList[i][0])

#print(availableMoveListNames)

moveExceptionNameList = []
moveExceptionMoveList = []

for line in monLines:
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    if(len(line) == 0):
        continue
    if(line[0] == ':' and line[-1] == "{" and line.find('preevo') == -1 and line.find('MegaForm') == -1 and line.find('OnCreation') == -1 and line.find('URSHIFITE') == -1):
        name = line[1:-5]
    if(compState and line.find(']') != -1):
        compState = False
        tmpList = line.replace(':', '')
        tmpList = tmpList.replace('[', '')
        tmpList = tmpList.replace(']', '')
        tmpList = tmpList.replace(' ', '')
        tmpList = tmpList.split(',')
        listedMoves = addToList(tmpList, listedMoves)
        continue
    if(line.find('compatiblemoves =>') != -1):
        if(line.find('Mew is') != -1):
            continue
        compState = True
        startLoc = line.find('>')
        tmpList = line[startLoc+1:-1].replace(':', '')
        tmpList = tmpList.replace('[', '')
        tmpList = tmpList.replace(']', '')
        tmpList = tmpList.replace(' ', '')
        tmpList = tmpList.split(',')
        listedMoves = addToList(tmpList, listedMoves)
        if(line.find(']') != -1):
            compState = False
        continue
    if(line.find('moveexceptions =>') != -1):
        if(line.find('[],') == -1):
            moveExceptionNameList.append(name)
            startLoc = line.find('>')
            tmpList = line[startLoc+1:-1].replace(':', '')
            tmpList = tmpList.replace('[', '')
            tmpList = tmpList.replace(']', '')
            tmpList = tmpList.replace(' ', '')
            tmpList = tmpList.split(',')
            moveExceptionMoveList.append(tmpList)
        continue


#print(moveExceptionNameList)
#print(moveExceptionMoveList)
#print(listedMoves)

unavailMoves = []
for i in range(len(listedMoves)):
    if(listedMoves[i] == 'LAVASURF'):
        listedMoves[i] = 'MAGMADRIFT'
    if(listedMoves[i] == ''):
        continue
    if(listedMoves[i] in availableMoveListNames):
        continue
    else:
        unavailMoves.append(listedMoves[i])

unavailMoves.append("CAPTIVATE")
unavailMoves.append("NATURALGIFT")
unavailMoves.sort()

unavailMovesList = []
for i in range(len(unavailMoves)):
    unavailMovesList.append([unavailMoves[i], "Unavailable", "Tutor"])

allMovesList = availableMoveList + unavailMovesList
#print(allMovesList)

allMovesListNames = []
for i in range(len(allMovesList)):
    if(i < 171): #TMs & HMs
        allMovesListNames.append(allMovesList[i][1])
    else:
        allMovesListNames.append(allMovesList[i][0])
#print(allMovesListNames)

universalMoves = ['Attract', 'Bide', 'Captivate', 'Confide', 'DoubleTeam', 'Endure', 'Facade', 'Frustration', 'HiddenPower', 'NaturalGift', 'Protect', 'Rest', 'Return', 'Round', 'SecretPower', 'SleepTalk', 'Snore', 'Substitute', 'Swagger', 'Toxic']

name = ''
newPok = False
for line in monLines:
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    if(len(line) == 0):
        continue
    if(line[0] == ':' and line[-1] == "{" and line.find('preevo') == -1 and line.find('MegaForm') == -1 and line.find('OnCreation') == -1 and line.find('URSHIFITE') == -1):
        newPok = True
        name = line[1:-5]
    if(compState and line.find(']') != -1):
        compState = False
        tmpList = line.replace(':', '')
        tmpList = tmpList.replace('[', '')
        tmpList = tmpList.replace(']', '')
        tmpList = tmpList.replace(' ', '')
        tmpList = tmpList.split(',')
        if(line.find(']') != -1):
            compState = False
        for i in range(len(tmpList)):
            if(tmpList[i] == ''):
                continue
            if(tmpList[i] == 'LAVASURF'):
                tmpList[i] = 'MAGMADRIFT'
            if(tmpList[i] == 'POUNCE'):
                continue
            curMoveIndex = allMovesListNames.index(tmpList[i])
            if(len(allMovesList[curMoveIndex]) == 3):
                allMovesList[curMoveIndex].append('"' + name + '",')
            else:
                allMovesList[curMoveIndex][3] = allMovesList[curMoveIndex][3] + '"' + name  + '",'
        continue
    if(line.find('compatiblemoves =>') != -1 and newPok):
        newPok = False
        if(line.find('Mew is') != -1): #Mew Exceptions
            pokIndex = moveExceptionNameList.index(name)
            pokMoveList = moveExceptionMoveList[pokIndex]
            for i in range(len(allMovesList)):
                if(allMovesList[i][0] in pokMoveList or allMovesList[i][0] == "POUNCE" or allMovesList[i][0] == 109):
                    continue
                if(len(allMovesList[i]) == 3):
                    allMovesList[i].append('"' + name + '",')
                else:
                    allMovesList[i][3] = allMovesList[i][3] + '"' + name  + '",'
            continue
        compState = True
        startLoc = line.find('>')
        tmpList = line[startLoc+1:-1].replace(':', '')
        tmpList = tmpList.replace('[', '')
        tmpList = tmpList.replace(']', '')
        tmpList = tmpList.replace(' ', '')
        tmpList = tmpList.split(',')
        if(line.find(']') != -1):
            compState = False
        for i in range(len(tmpList)):
            if(tmpList[i] == ''):
                continue
            if(tmpList[i] == 'LAVASURF'):
                tmpList[i] = 'MAGMADRIFT'
            if(tmpList[i] == 'POUNCE'):
                continue
            curMoveIndex = allMovesListNames.index(tmpList[i])
            if(len(allMovesList[curMoveIndex]) == 3):
                allMovesList[curMoveIndex].append('"' + name + '",')
            else:
                allMovesList[curMoveIndex][3] = allMovesList[curMoveIndex][3] + '"' + name  + '",'
        for i in range(len(universalMoves)):
            if(name in moveExceptionNameList):
                pokIndex = moveExceptionNameList.index(name)
                pokMoveList = moveExceptionMoveList[pokIndex]
                curMoveIndex = allMovesListNames.index(universalMoves[i].upper())
                if(universalMoves[i].upper() in pokMoveList):
                    continue
                if(len(allMovesList[curMoveIndex]) == 3):
                    allMovesList[curMoveIndex].append('"' + name + '",')
                else:
                    allMovesList[curMoveIndex][3] = allMovesList[curMoveIndex][3] + '"' + name  + '",'
                continue
            else:
                curMoveIndex = allMovesListNames.index(universalMoves[i].upper())
                if(len(allMovesList[curMoveIndex]) == 3):
                    allMovesList[curMoveIndex].append('"' + name + '",')
                else:
                    allMovesList[curMoveIndex][3] = allMovesList[curMoveIndex][3] + '"' + name  + '",'
                continue

#print(allMovesList[18][1])

#Actually starting to write the file lmao
fullText = 'local TMs = {\n'
fullText += '--Current Sorting:\n'
fullText += '--TMs/HMs\n'
fullText += '--Available Tutors\n'
fullText += '--Unavailable Moves\n\n'

for i in range(len(allMovesList)):
    if(len(allMovesList[i]) < 4):
        #print(str(allMovesList[i][0]))
        if(allMovesList[i][0] == 109):
            fullText += '[109]={"???", "TM109"},\n'
        continue
    if(i < 172):
        fullText += '[' + str(allMovesList[i][0]) + ']=\n{'
    else:
        fullText += '["' + allMovesList[i][0] + '"]=\n{'
    fullText += '"' + allMovesList[i][1] + '","' + allMovesList[i][2] + '",' + allMovesList[i][3][:-1]
    fullText += '},\n'

fullText += '}\nreturn TMs'

newFile = open("Outputs/DatabaseTMs.txt", "w")
newFile.write(fullText)
newFile.close()
itemFile.close()
monFile.close()
