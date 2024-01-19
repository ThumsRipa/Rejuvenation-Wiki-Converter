import numpy as np
import pandas as pd

#Note: Flabébé causes issues due to the weird accents. May need to edit the name manually

monFile = open('RBFiles/montext.rb', "r", encoding='utf8')
abilFile = open('RBFiles/abiltext.rb', "r", encoding='utf8')
itemFile = open('RBFiles/itemtext.rb', "r", encoding='utf8')
monLines = monFile.readlines()
abilLines = abilFile.readlines()
itemLines = itemFile.readlines()

fulltext = 'local p = {\n["none"] = nil,\n'

allAbils = []
abilNick = ''
abilFull = ''

#Start with Abilities
for line in abilLines:
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    line = line.replace('\\', '')
    line = line.replace("\'", "'") #Dragon's Maw is the only one breaking
    if(line == ''):
        continue
    if(line[0] == ':' and line[-1] == '{'):
        endLoc = line.find('=')
        abilNick = line[1:endLoc-1]
        continue
    if(line.find('name =>') != -1):
        startLoc = line.find('>')
        abilFull = line[startLoc+2:-1]
        continue
    if(line.find('fullName =>') != -1):
        startLoc = line.find('>')
        abilFull = line[startLoc+2:-1]
        continue
    if(line == '},'):
        allAbils.append([abilNick, abilFull])
allAbils.sort()

fulltext += '-----------------------------------------------Abilities\n'
for i in range(len(allAbils)):
    fulltext += '["' + allAbils[i][0] + '"]=' + allAbils[i][1] + ',\n'

#Now Items
allItems = []
itemNick = ''
itemFull = ''

for line in itemLines:
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    line = line.replace('\\', '')
    if(line == ''):
        continue
    if(line[0] == ':' and line[-1] == '{'):
        endLoc = line.find('=')
        itemNick = line[1:endLoc-1]
        continue
    if(line.find('name =>') != -1):
        startLoc = line.find('>')
        itemFull = line[startLoc+2:-1]
        continue
    if(line.find('fullName =>') != -1):
        startLoc = line.find('>')
        itemFull = line[startLoc+2:-1]
        continue
    if(line == '},'):
        allItems.append([itemNick, itemFull])
allItems.sort()

fulltext += '-----------------------------------------------Items\n'
for i in range(len(allItems)):
    fulltext += '["' + allItems[i][0] + '"]=' + allItems[i][1] + ',\n'

#Finally, Pokemon
allNames = []
namesCaps = ''
namesNorm = ''
foundAll = False

for line in monLines:
    line = line.replace('\t', '')
    line = line.replace('\n', '')
    if(len(line) == 0):
        continue
    if(line[0] == ':' and line[-1] == "{" and line.find('preevo') == -1 and line.find('MegaForm') == -1 and line.find('OnCreation') == -1 and line.find('URSHIFITE') == -1):
        namesCaps = line[1:-5]
        foundAll = False
    if(foundAll):
        continue
    if(line.find('name =>') != -1):
        foundAll = True
        startLoc = line.find('>')
        namesNorm = line[startLoc+2:-1]
        allNames.append([namesCaps, namesNorm])

allNames.sort()

fulltext += '-----------------------------------------------Species\n'
for i in range(len(allNames)):
    fulltext += '["' + allNames[i][0] + '"]=' + allNames[i][1] + ',\n'

fulltext += '-----------------------------------------------Species, Reversed\n'
for i in range(len(allNames)):
    fulltext += '[' + allNames[i][1] + ']="' + allNames[i][0] + '",\n'

fulltext += '}\nreturn p'

newFile = open("Outputs/DatabaseNames.txt", "w", encoding="utf-8")
newFile.write(fulltext)
newFile.close()

monFile.close()
abilFile.close()
itemFile.close()