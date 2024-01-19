import numpy as np
import pandas as pd

moveFile = open('RBFiles/movetext.rb', "r", encoding='utf8')
moveLines = moveFile.readlines()

def makeLines(fullName, dataPairs, moveDataFlags, moveAffectFlags):
    tmpText = '["' + fullName + '"]={\n'
    for i in range(len(dataPairs)):
        tmpText += '\t' + dataPairs[i][0] + '=' + dataPairs[i][1] + ',\n'
    if(len(moveDataFlags) > 0):
        tmpText += '\tDataFlags={'
        for i in range(len(moveDataFlags)):
            tmpText += '"' + moveDataFlags[i] + '",'
        tmpText = tmpText[:-1] + '},\n'
    if(len(moveAffectFlags) > 0):
        tmpText += '\tMoveFlags={'
        for i in range(len(moveAffectFlags)):
            tmpText += '"' + moveAffectFlags[i] + '",'
        tmpText = tmpText[:-1] + '},\n'
    return tmpText + '},\n'

moveData = []
dataFlags = []
moveFlags = []
named = False

fulltxt = '--Database of all moves in Rejuvenation'
fulltxt += '--Things that changed:\n'
fulltxt += '--Not all moves will have a "Chance" or "Priority" tag\n'
fulltxt += '--"Target" is now a string instead of a two digit value\n'
fulltxt += '--General "Flags" are gone, instead replaced by a line for DataFlags and MoveFlags\n'
fulltxt += '--DataFlags are things that categorize the move (Punch move, sound move, z-move, etc)\n'
fulltxt += '--MoveFlags are how other moves (or items) can affect it (King\'s Rock, Protect, Snatch)\n\n'
fulltxt += 'local Moves = {\n'

for line in moveLines:
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    if(len(line) == 0):
        continue
    if(line.find('# MOVE DUMMIES FOR ANIMATION COMPILATION') != -1):
        break
    if(line.find('#') != -1 or line.find('MOVEHASH = ') != -1):
        continue
    if(line == '},'):
        fulltxt += makeLines(nameCap, moveData, dataFlags, moveFlags)
        moveData = []
        dataFlags = []
        moveFlags = []
        named = False
        continue
    if(line.find(':') != -1 and line.find('{') != -1):
        startLoc = line.find(':')
        endLoc = line.find('=')
        if(line[endLoc-1] == ' '):
            nameCap = line[startLoc+1:endLoc-1]
        else:
            nameCap = line[startLoc+1:endLoc]
            #print(nameCap)
        #print(nameCap)
        continue
    if(line.find(':ID =>') != -1):
        continue
    if(line.find(':name =>') != -1):
        startLoc = line.find('>')
        moveData.append(['MoveName', line[startLoc+2:-1]])
        named = True
        continue
    if(line.find(':longname =>') != -1):
        if not named:
            startLoc = line.find('>')
            moveData.append(['MoveName', line[startLoc+2:-1]])
            named = True
        else:
            moveData.pop()
            startLoc = line.find('>')
            moveData.append(['MoveName', line[startLoc+2:-1]])
        continue
    if(line.find(':function =>') != -1):
        startLoc = line.find('0x')
        moveData.append(['Effect', '"' + line[startLoc+2:-1] + '"'])
        continue
    if(line.find(':type =>') != -1):
        startLoc = line.find('>')
        moveData.append(['Type', '"' + line[startLoc+2:-1].replace(':', '') + '"'])
        continue
    if(line.find(':category =>') != -1):
        startLoc = line.find('>')
        moveData.append(['Category', '"' + line[startLoc+2:-1].replace(':', '').capitalize() + '"'])
        continue
    if(line.find(':basedamage =>') != -1):
        startLoc = line.find('>')
        moveData.append(['Strength', '"' + line[startLoc+2:-1] + '"'])
        continue
    if(line.find(':accuracy =>') != -1):
        startLoc = line.find('>')
        moveData.append(['Accuracy', '"' + line[startLoc+2:-1] + '"'])
        continue
    if(line.find(':maxpp =>') != -1):
        startLoc = line.find('>')
        moveData.append(['PP', '"' + line[startLoc+2:-1] + '"'])
        continue
    if(line.find(':effect =>') != -1):
        startLoc = line.find('>')
        moveData.append(['Chance', '"' + line[startLoc+2:-1] + '"'])
        continue
    if(line.find(':moreeffect =>') != -1): #moves with two effects like fang moves and triple arrow (just those actually)
        startLoc = line.find('>')
        moveData.append(['SecondChance', '"' + line[startLoc+2:-1] + '"'])
        continue
    if(line.find(':target =>') != -1):
        startLoc = line.find('>')
        moveData.append(['Target', '"' + line[startLoc+2:-1].replace(':', '') + '"'])
        continue
    if(line.find(':priority =>') != -1):
        startLoc = line.find('>')
        moveData.append(['Priority', '"' + line[startLoc+2:-1].replace(':', '') + '"'])
        continue
    if(line.find(':desc =>') != -1):
        startLoc = line.find('>')
        line = line.replace('Pokémon', 'Pokemon')
        line = line.replace('pokémon', 'Pokemon')
        line = line.replace('’', "'")
        line = line.replace('—', ' - ')
        
        
        if(line[-1] == '"'):
            moveData.append(['Description', line[startLoc+2:]])
        else:
            moveData.append(['Description', line[startLoc+2:-1]])
        continue
    #End General Move Information. Below are flags for data purposes
    if(line.find(':zmove =>') != -1):
        dataFlags.append('ZMove')
        continue
    if(line.find(':intercept =>') != -1):
        dataFlags.append('InterceptMove')
        continue
    if(line.find(':contact =>') != -1): #Is a contact move
        dataFlags.append('Contact')
        continue
    if(line.find(':soundmove =>') != -1):
        dataFlags.append('Sound')
        continue
    if(line.find(':sharpmove =>') != -1):
        dataFlags.append('Sharp')
        continue
    if(line.find(':healingmove =>') != -1):
        dataFlags.append('Healing')
        continue
    if(line.find(':punchmove =>') != -1):
        dataFlags.append('Punch')
        continue
    if(line.find(':windmove =>') != -1):
        dataFlags.append('Wind')
        continue
    if(line.find(':beammove =>') != -1):
        dataFlags.append('Beam')
        continue
    if(line.find(':heavymove =>') != -1):
        dataFlags.append('Beam')
        continue
    if(line.find(':highcrit =>') != -1):
        dataFlags.append('HighCrit')
        continue
    if(line.find(':recoil =>') != -1):
        dataFlags.append('Recoil')
        continue


    #Below are extra flags for what can affect the move. Not used by the wiki at the moment
    if(line.find(':kingrock =>') != -1): #Affected by King's Rock
        moveFlags.append('Kingrock')
        continue
    if(line.find(':bypassprotect =>') != -1): #Cannot be blocked by Protect
        moveFlags.append('NoProtect')
        continue
    if(line.find(':defrost =>') != -1): #Defrosts the target
        moveFlags.append('Defrost')
        continue
    if(line.find(':nonmirror =>') != -1): #Cannot be mirror moved
        dataFlags.append('NoMirror')
        continue
    if(line.find(':snatchable =>') != -1): #Can be snatched
        dataFlags.append('Snachable')
        continue
    if(line.find(':magiccoat =>') != -1): #Can be reflected by magic coat
        dataFlags.append('MagicCoat')
        continue
    if(line.find(':gravityblocked =>') != -1): #Blocked by Gravity
        dataFlags.append('GraviyBlocked')
        continue


    endLoc = line.find('=')
    #print(line[1: endLoc-1])
fulltxt += '}\nreturn Moves'

newFile = open("Outputs/DatabaseMoves.txt", "w")
newFile.write(fulltxt)
newFile.close()
moveFile.close()