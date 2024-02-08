import numpy as np
import pandas as pd

mapFile = open('RBFiles/metatext.rb', "r", encoding='utf8')
mapLines = mapFile.readlines()

off = True #Checking variable if we are at the maps yet (skipping all the initial stuff with trainer tags)

fulltext = 'local Database = {\n["000"] = {\n\tName="None",\n},\n'

mapName = ''
mapNum = ''
numCheck = 1 #Check if all map numbers are present

for line in mapLines:
    if(line[0] != '#' and off):
        continue
    else:
        off=False
    line = line.replace('\n', '')
    line = line.replace('\\', '')
    if(len(line) == 0 or line[0] == '\t' or line[0] == ' '):
        continue
    if(line[0] == '#'):
        mapName = line[1:]
        while(mapName[-1] == ' '):
            mapName = mapName[:-1]
        continue
    elif(line.find('=> {') != -1):
        endLoc = line.find('=')
        mapNum = line[0:endLoc-1]
        if(numCheck != int(mapNum)):
            print('Map Number ' + str(numCheck) + 'Missing')
            while(numCheck != int(mapNum)):
                numCheck += 1
        else:
            numCheck += 1
        if(len(mapNum) < 2):
            mapNum = '00' + mapNum
        elif(len(mapNum) < 3):
            mapNum = '0' + mapNum
        continue
    elif(line.find('},') != -1):
        fulltext += '["' + mapNum + '"] = {\n\tName="' + mapName + '",\n},\n'
        #print(mapName + ' ' + mapNum)
        mapName = ''
        mapNum = ''
        continue

fulltext += '}\n\nreturn Database'
newFile = open("Outputs/DatabaseMaps.txt", "w", encoding="utf-8")
newFile.write(fulltext)
newFile.close()
mapFile.close()